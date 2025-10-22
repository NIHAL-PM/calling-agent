# AI Calling Agent Demo System

## 🎯 Complete Multi-Service Call Center with Live Dashboard

This is a production-ready demo of an AI-powered calling agent system with 5 fully functional services that your clients can actually call and interact with.

### 📞 Available Services

1. **🍔 GourmetEats Restaurant** - `+1-555-FOOD-001`
   - Order food with menu browsing
   - Handles special requests
   - Provides order IDs and delivery times

2. **🏥 HealthCare Plus Hospital** - `+1-555-HEAL-002`
   - Book medical appointments
   - Department selection
   - Emergency handling with crisis numbers

3. **💻 TechFix Support** - `+1-555-TECH-003`
   - Technical troubleshooting
   - Step-by-step guidance
   - Ticket generation

4. **✈️ SkyHigh Travel Agency** - `+1-555-TRIP-004`
   - Flight and hotel booking
   - Destination recommendations
   - Booking confirmations

5. **📞 Universal Customer Service** - `+1-555-HELP-005`
   - General inquiries
   - Returns and refunds
   - Account management

### 🚀 Setup Instructions

1. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Set Gemini API Key**
   ```powershell
   $env:GEMINI_API_KEY = "your-api-key-here"
   ```

3. **Run the Application**
   ```powershell
   python app.py
   ```

4. **Open Dashboard**
   - Navigate to: `http://localhost:5000`
   - Click any service card to start a call
   - Allow microphone access when prompted

### 🎨 Dashboard Features

- **Live Call Interface**: Real-time audio conversation with AI agents
- **Call Transcripts**: See conversation history as it happens
- **Service Cards**: Color-coded, interactive service selection
- **Real-time Stats**: Track total calls, active calls, orders, etc.
- **Data Tracking**: 
  - Food orders with order IDs
  - Hospital appointments
  - Support tickets
  - Complete call logs

### 🎤 How to Use

1. Click "Call Now" on any service card
2. Allow microphone access
3. Speak naturally - the AI will respond with voice
4. View live transcript of the conversation
5. The AI handles:
   - Taking orders/bookings
   - Answering questions
   - Processing requests
   - Generating confirmation numbers
6. Click "End Call" when done
7. Check the tabs below to see stored data

### 📊 Admin Dashboard Tabs

- **Call Logs**: All calls with timestamps and status
- **Food Orders**: Restaurant orders with IDs
- **Appointments**: Hospital bookings
- **Support Tickets**: Tech support cases

### 🎭 Demo Mode Features

Each AI agent has a specialized master prompt that:
- Handles service-specific tasks
- Maintains professional tone
- Extracts structured data (order IDs, ticket numbers, etc.)
- Stores data in appropriate databases
- Provides realistic responses

### 🔧 Technical Stack

- **Backend**: Flask + SocketIO (Real-time communication)
- **AI**: Google Gemini 2.5 Flash (Native audio + dialog)
- **Audio**: PyAudio (16kHz input, 24kHz output)
- **Frontend**: Vanilla JS + WebSockets
- **Real-time**: Bidirectional audio streaming

### 🎯 Perfect for Client Demos

This system is ready to showcase:
- Multiple service types in one platform
- Real voice conversations (not text-to-speech)
- Live transcription
- Data extraction and storage
- Professional UI/UX
- Scalable architecture

### 📝 Customization

To add more services, edit `app.py`:

1. Add to `SERVICES` dict with phone number, color, icon
2. Add master prompt to `MASTER_PROMPTS` dict
3. Define what data to extract in `extract_call_data()`

### 🔐 Security Notes

For production deployment:
- Change the SECRET_KEY in app.py
- Use environment variables for API keys
- Add authentication/authorization
- Enable HTTPS
- Rate limit API calls

### 💡 Tips for Best Demo

1. Use headphones to prevent echo
2. Speak clearly near your microphone
3. Let the AI finish speaking before responding
4. Try different services to show versatility
5. Check the dashboard tabs to show data tracking

---

**Built with ❤️ for impressive client demonstrations**
