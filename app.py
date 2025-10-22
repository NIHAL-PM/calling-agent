"""
Multi-Service AI Calling Agent Dashboard
=========================================
A complete demo system with multiple AI agents handling different services:
- Restaurant Food Ordering
- Hospital Appointment Booking
- Tech Support
- Travel Booking
- General Customer Service
"""

from flask import Flask, render_template, jsonify, request, session
from flask_socketio import SocketIO, emit
import os
import asyncio
import base64
import io
import json
from datetime import datetime
from google import genai
from google.genai import types
import pyaudio
import threading
import queue
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'demo-secret-key-change-in-production')
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Initialize Gemini client
client = genai.Client(
    http_options={"api_version": "v1beta"},
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

# Service configurations with phone numbers
SERVICES = {
    "restaurant": {
        "name": "GourmetEats Restaurant",
        "phone": "+1-555-FOOD-001",
        "color": "#FF6B6B",
        "icon": "🍔",
        "description": "Order delicious food"
    },
    "hospital": {
        "name": "HealthCare Plus Hospital",
        "phone": "+1-555-HEAL-002",
        "color": "#4ECDC4",
        "icon": "🏥",
        "description": "Book appointments"
    },
    "techsupport": {
        "name": "TechFix Support Center",
        "phone": "+1-555-TECH-003",
        "color": "#95E1D3",
        "icon": "💻",
        "description": "Get technical help"
    },
    "travel": {
        "name": "SkyHigh Travel Agency",
        "phone": "+1-555-TRIP-004",
        "color": "#F38181",
        "icon": "✈️",
        "description": "Book flights & hotels"
    },
    "support": {
        "name": "Universal Customer Service",
        "phone": "+1-555-HELP-005",
        "color": "#AA96DA",
        "icon": "📞",
        "description": "General inquiries"
    }
}

# Master prompts for each service
MASTER_PROMPTS = {
    "restaurant": """
You are an AI assistant for GourmetEats Restaurant. Your job is to:
1. Greet customers warmly
2. Help them browse the menu (Pizza, Burgers, Pasta, Salads, Desserts)
3. Take their order with quantities
4. Confirm delivery address
5. Provide estimated delivery time (30-45 minutes)
6. Process payment confirmation
7. Give order ID at the end

Be friendly, suggest popular items, handle special requests (extra cheese, no onions, etc.).
Example menu items with prices:
- Margherita Pizza: $12.99
- Cheeseburger Deluxe: $9.99
- Spaghetti Carbonara: $14.99
- Caesar Salad: $7.99
- Chocolate Cake: $5.99

Always confirm the complete order before finalizing.
""",
    
    "hospital": """
You are an AI receptionist for HealthCare Plus Hospital. Your responsibilities:
1. Greet patients professionally
2. Ask about their medical concern (general checkup, specialist visit, emergency)
3. Recommend appropriate doctor/department
4. Check available time slots (weekdays 9 AM - 5 PM)
5. Collect patient name, phone, insurance info
6. Confirm appointment date and time
7. Provide appointment ID

Available departments: Cardiology, Orthopedics, Pediatrics, General Medicine, Emergency.
Be empathetic, professional, and prioritize urgent cases.
For emergencies, immediately provide emergency number: 911
""",
    
    "techsupport": """
You are a technical support agent for TechFix Support. Your goals:
1. Greet customer and get their name
2. Identify the issue (software, hardware, network, account)
3. Ask diagnostic questions
4. Provide step-by-step troubleshooting
5. Offer remote assistance if needed
6. Create support ticket with issue ID

Common issues: WiFi problems, software installation, password reset, device not working.
Be patient, explain in simple terms, and confirm each step is completed.
Always provide a ticket number at the end: TECH-XXXXX
""",
    
    "travel": """
You are a travel booking agent for SkyHigh Travel Agency. Your tasks:
1. Greet the customer warmly
2. Ask for travel preferences (destination, dates, budget)
3. Suggest flight options with prices
4. Offer hotel packages
5. Handle special requests (window seat, dietary needs)
6. Process booking with confirmation
7. Provide booking reference number

Popular destinations: New York, Paris, Tokyo, Dubai, London.
Be enthusiastic, suggest deals, and ensure customer satisfaction.
Flight prices range from $299 to $1,500. Hotels from $100-$400 per night.
""",
    
    "support": """
You are a general customer service agent for Universal Customer Service. You handle:
1. Product inquiries
2. Return/refund requests
3. Account issues
4. Billing questions
5. General complaints
6. Feedback collection

Be professional, empathetic, and solution-oriented.
Always get: customer name, order/account number, issue description.
Provide resolution steps and ticket number.
For escalations, mention: "I'll connect you with a supervisor."
"""
}

# Store active calls and their data
active_calls = {}
call_logs = []
orders_db = []
appointments_db = []
support_tickets = []

class AICallAgent:
    def __init__(self, service_type, call_id):
        self.service_type = service_type
        self.call_id = call_id
        self.session = None
        self.audio_in_queue = queue.Queue()
        self.is_active = True
        self.transcript = []
        self.call_data = {
            "service": service_type,
            "start_time": datetime.now().isoformat(),
            "status": "active",
            "transcript": [],
            "metadata": {}
        }
        
    async def start_session(self):
        """Initialize the AI session"""
        config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore" if self.service_type in ["hospital", "support"] else "Puck"
                    )
                )
            ),
        )
        
        self.session = await client.aio.live.connect(
            model="models/gemini-2.5-flash-preview-native-audio-dialog",
            config=config
        )
        
        # Send master prompt
        prompt = MASTER_PROMPTS.get(self.service_type, MASTER_PROMPTS["support"])
        await self.session.send(input=prompt, end_of_turn=True)
        
        # Start greeting
        greeting = f"Hello! Thank you for calling {SERVICES[self.service_type]['name']}. How may I assist you today?"
        self.add_to_transcript("Agent", greeting)
        socketio.emit('call_transcript', {
            'call_id': self.call_id,
            'speaker': 'Agent',
            'text': greeting
        })
        
    async def process_audio(self, audio_data):
        """Process incoming audio from user"""
        if self.session and self.is_active:
            await self.session.send(input={"data": audio_data, "mime_type": "audio/pcm"})
    
    async def receive_responses(self):
        """Receive and process AI responses"""
        while self.is_active and self.session:
            try:
                turn = self.session.receive()
                async for response in turn:
                    if data := response.data:
                        # Send audio back to client
                        socketio.emit('audio_data', {
                            'call_id': self.call_id,
                            'data': base64.b64encode(data).decode()
                        })
                    if text := response.text:
                        self.add_to_transcript("Agent", text)
                        socketio.emit('call_transcript', {
                            'call_id': self.call_id,
                            'speaker': 'Agent',
                            'text': text
                        })
                        # Extract and store structured data
                        self.extract_call_data(text)
            except Exception as e:
                print(f"Error in receive_responses: {e}")
                break
    
    def add_to_transcript(self, speaker, text):
        """Add to transcript"""
        entry = {
            "speaker": speaker,
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
        self.transcript.append(entry)
        self.call_data["transcript"].append(entry)
    
    def extract_call_data(self, text):
        """Extract structured data from conversation"""
        text_lower = text.lower()
        
        # Extract order details for restaurant
        if self.service_type == "restaurant":
            if "order id" in text_lower or "order number" in text_lower:
                import re
                order_id = re.search(r'(?:order (?:id|number)[:\s]+)?([A-Z0-9-]+)', text, re.IGNORECASE)
                if order_id:
                    self.call_data["metadata"]["order_id"] = order_id.group(1)
        
        # Extract appointment details for hospital
        elif self.service_type == "hospital":
            if "appointment" in text_lower:
                self.call_data["metadata"]["has_appointment"] = True
        
        # Extract ticket ID for support
        elif self.service_type == "techsupport":
            if "ticket" in text_lower or "tech-" in text_lower:
                import re
                ticket = re.search(r'TECH-\d+', text, re.IGNORECASE)
                if ticket:
                    self.call_data["metadata"]["ticket_id"] = ticket.group(0)
    
    async def end_call(self):
        """End the call session"""
        self.is_active = False
        self.call_data["end_time"] = datetime.now().isoformat()
        self.call_data["status"] = "completed"
        
        # Store in appropriate database
        if self.service_type == "restaurant" and "order_id" in self.call_data["metadata"]:
            orders_db.append(self.call_data)
        elif self.service_type == "hospital":
            appointments_db.append(self.call_data)
        else:
            support_tickets.append(self.call_data)
        
        call_logs.append(self.call_data)
        
        if self.session:
            await self.session.close()

# Flask routes
@app.route('/')
def index():
    return render_template('dashboard.html', services=SERVICES)

@app.route('/dialer')
def dialer():
    return render_template('dialer.html')

@app.route('/mic-test')
def mic_test():
    return render_template('mic_test.html')

@app.route('/api/services')
def get_services():
    return jsonify(SERVICES)

@app.route('/api/call-logs')
def get_call_logs():
    return jsonify(call_logs)

@app.route('/api/orders')
def get_orders():
    return jsonify(orders_db)

@app.route('/api/appointments')
def get_appointments():
    return jsonify(appointments_db)

@app.route('/api/tickets')
def get_tickets():
    return jsonify(support_tickets)

@app.route('/api/stats')
def get_stats():
    return jsonify({
        "total_calls": len(call_logs),
        "active_calls": len(active_calls),
        "total_orders": len(orders_db),
        "total_appointments": len(appointments_db),
        "total_tickets": len(support_tickets)
    })

# SocketIO events
@socketio.on('start_call')
def handle_start_call(data):
    service_type = data.get('service')
    call_id = f"{service_type}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    agent = AICallAgent(service_type, call_id)
    active_calls[call_id] = agent
    
    # Start agent in background
    def run_agent():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(agent.start_session())
        loop.run_until_complete(agent.receive_responses())
    
    thread = threading.Thread(target=run_agent)
    thread.start()
    
    emit('call_started', {
        'call_id': call_id,
        'service': SERVICES[service_type]
    })

@socketio.on('send_audio')
def handle_audio(data):
    call_id = data.get('call_id')
    audio_data = base64.b64decode(data.get('audio'))
    
    if call_id in active_calls:
        agent = active_calls[call_id]
        # Process audio in background
        asyncio.run(agent.process_audio(audio_data))

@socketio.on('end_call')
def handle_end_call(data):
    call_id = data.get('call_id')
    
    if call_id in active_calls:
        agent = active_calls[call_id]
        asyncio.run(agent.end_call())
        del active_calls[call_id]
        
        emit('call_ended', {
            'call_id': call_id,
            'summary': agent.call_data
        })

@socketio.on('user_speech')
def handle_user_speech(data):
    """Handle transcribed user speech"""
    call_id = data.get('call_id')
    text = data.get('text')
    
    if call_id in active_calls:
        agent = active_calls[call_id]
        agent.add_to_transcript("User", text)
        
        # Broadcast to all clients
        emit('call_transcript', {
            'call_id': call_id,
            'speaker': 'User',
            'text': text
        }, broadcast=True)

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Multi-Service AI Calling Agent System Starting...")
    print("=" * 60)
    print("\n📞 Available Services:")
    for key, service in SERVICES.items():
        print(f"  {service['icon']} {service['name']}: {service['phone']}")
    print("\n🌐 Dashboard URLs:")
    print("   • HTTPS: https://localhost:5000 (Secure - Required for microphone)")
    print("   • HTTP:  http://localhost:5000 (Fallback)")
    print("\n⚠️  Note: Your browser will show a security warning for the")
    print("   self-signed certificate. Click 'Advanced' and 'Proceed' to continue.")
    print("\n📱 Phone Dialer: https://localhost:5000/dialer")
    print("=" * 60)
    
    # Run with HTTPS using adhoc SSL context
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, ssl_context='adhoc')
