"""
Demo Script Runner - Simulates realistic conversations with each service
This is useful for testing or pre-recording demos
"""

import asyncio
import os
from google import genai
from google.genai import types

client = genai.Client(
    http_options={"api_version": "v1beta"},
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# Demo conversations for each service
DEMO_SCRIPTS = {
    "restaurant": [
        ("User", "Hi, I'd like to order some food for delivery."),
        ("User", "What pizzas do you have?"),
        ("User", "I'll take a large Margherita pizza and a Caesar salad."),
        ("User", "Yes, extra cheese on the pizza please."),
        ("User", "123 Main Street, Apartment 4B."),
        ("User", "Yes, that's correct."),
        ("User", "Card payment is fine. Thank you!"),
    ],
    
    "hospital": [
        ("User", "Hello, I need to book an appointment."),
        ("User", "I've been having chest pains occasionally."),
        ("User", "How about next Tuesday at 2 PM?"),
        ("User", "My name is John Smith, phone number 555-0123."),
        ("User", "Yes, I have BlueCross insurance."),
        ("User", "Thank you, see you then!"),
    ],
    
    "techsupport": [
        ("User", "Hi, my computer won't connect to WiFi."),
        ("User", "Windows 11, and it was working yesterday."),
        ("User", "I can see the network name but it won't connect."),
        ("User", "Okay, I'll try that... Yes, I restarted the router."),
        ("User", "It's working now! Thank you so much!"),
    ],
    
    "travel": [
        ("User", "I want to book a flight to Paris."),
        ("User", "Leaving next month, around the 15th, returning on the 22nd."),
        ("User", "Economy class is fine. What's available?"),
        ("User", "The morning flight sounds good."),
        ("User", "Yes, please also recommend a hotel."),
        ("User", "The one near the Eiffel Tower sounds perfect!"),
    ],
    
    "support": [
        ("User", "I need help with my recent order."),
        ("User", "My order number is ORD-12345."),
        ("User", "I received the wrong item."),
        ("User", "I ordered a blue shirt but received a red one."),
        ("User", "Yes, I'd like to return it for the correct item."),
        ("User", "Thank you for your help!"),
    ]
}

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

Always confirm the complete order before finalizing. Provide order ID like: ORD-FOOD-001
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
Provide appointment ID like: APT-HEAL-001
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
Always provide a ticket number at the end: TECH-12345
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
Provide booking reference like: BKG-TRIP-001
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
Provide resolution steps and ticket number like: TKT-HELP-001
For escalations, mention: "I'll connect you with a supervisor."
"""
}

async def run_demo_conversation(service_name):
    """Run a demo conversation for a specific service"""
    print("\n" + "=" * 70)
    print(f"🎬 Starting Demo Conversation: {service_name.upper()}")
    print("=" * 70)
    
    config = types.LiveConnectConfig(
        response_modalities=["TEXT"],  # Text only for demo
    )
    
    async with client.aio.live.connect(
        model="models/gemini-2.5-flash-preview-native-audio-dialog",
        config=config
    ) as session:
        # Send master prompt
        prompt = MASTER_PROMPTS.get(service_name, "You are a helpful assistant.")
        await session.send(input=prompt, end_of_turn=True)
        
        # Initial greeting
        print("\n🤖 Agent: (Greeting customer...)")
        turn = session.receive()
        async for response in turn:
            if text := response.text:
                print(f"🤖 Agent: {text}")
        
        # Run through demo script
        for speaker, line in DEMO_SCRIPTS.get(service_name, []):
            await asyncio.sleep(2)  # Pause between exchanges
            
            print(f"\n👤 {speaker}: {line}")
            await session.send(input=line, end_of_turn=True)
            
            # Get response
            turn = session.receive()
            async for response in turn:
                if text := response.text:
                    print(f"🤖 Agent: {text}")
        
        print("\n✅ Demo conversation completed!")
        print("=" * 70)

async def run_all_demos():
    """Run demos for all services"""
    print("\n" + "🎯" * 35)
    print("      AI CALLING AGENT SYSTEM - FULL DEMO")
    print("🎯" * 35)
    
    services = ["restaurant", "hospital", "techsupport", "travel", "support"]
    
    for i, service in enumerate(services, 1):
        print(f"\n\n📞 Demo {i}/{len(services)}")
        await run_demo_conversation(service)
        
        if i < len(services):
            print("\n⏳ Preparing next demo...")
            await asyncio.sleep(3)
    
    print("\n\n" + "🎉" * 35)
    print("      ALL DEMOS COMPLETED!")
    print("🎉" * 35)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        service = sys.argv[1].lower()
        if service in DEMO_SCRIPTS:
            print(f"\n🎬 Running single demo: {service}")
            asyncio.run(run_demo_conversation(service))
        else:
            print(f"❌ Unknown service: {service}")
            print(f"Available: {', '.join(DEMO_SCRIPTS.keys())}")
    else:
        print("\n🎬 Running all demos...")
        print("Tip: Run 'python demo_runner.py restaurant' to test a single service")
        asyncio.run(run_all_demos())
