# 🚀 Complete Setup Guide for AI Calling Agent Demo

## Step-by-Step Installation

### 1️⃣ Prerequisites

- **Python 3.8 or higher** 
  - Download from: https://www.python.org/downloads/
  - ✅ Make sure to check "Add Python to PATH" during installation

- **Microphone Access**
  - Your browser will need permission to access the microphone
  - Headphones recommended to prevent echo

- **Gemini API Key**
  - Get free API key: https://aistudio.google.com/app/apikey
  - Sign in with Google account
  - Click "Create API Key"
  - Copy the key

### 2️⃣ Installation

#### Option A: Quick Start (Recommended)

1. Open PowerShell in the project folder
2. Run the start script:
   ```powershell
   .\start.ps1
   ```
3. Enter your API key when prompted
4. Wait for dependencies to install
5. Dashboard will open automatically

#### Option B: Manual Installation

1. **Set API Key**
   ```powershell
   $env:GEMINI_API_KEY = "your-api-key-here"
   ```

2. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Handle PyAudio (if needed)**
   
   If PyAudio fails to install:
   - Download wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
   - Choose correct version (e.g., `PyAudio-0.2.14-cp311-cp311-win_amd64.whl` for Python 3.11)
   - Install: `pip install PyAudio-0.2.14-cp311-cp311-win_amd64.whl`

4. **Run the Application**
   ```powershell
   python app.py
   ```

5. **Open Dashboard**
   - Navigate to: http://localhost:5000

### 3️⃣ Testing the System

#### Quick Test Script
```powershell
python test_system.py
```

This will verify:
- API endpoints are working
- All 5 services are configured
- Dashboard is accessible

#### Demo Runner (Text-based)
```powershell
# Test all services
python demo_runner.py

# Test specific service
python demo_runner.py restaurant
python demo_runner.py hospital
```

### 4️⃣ Using the Dashboard

1. **Select a Service**
   - Click any of the 5 service cards
   - Each has a unique phone number and purpose

2. **Make a Call**
   - Click "Call Now" button
   - Allow microphone access when prompted
   - Speak naturally to the AI agent

3. **During the Call**
   - Watch live transcript appear
   - Use Mute button if needed
   - Click "End Call" when finished

4. **View Results**
   - Check "Call Logs" tab for all calls
   - Check "Food Orders" for restaurant orders
   - Check "Appointments" for hospital bookings
   - Check "Support Tickets" for tech support cases

### 5️⃣ The 5 Services Explained

#### 🍔 GourmetEats Restaurant (+1-555-FOOD-001)
**Try saying:**
- "I'd like to order a pizza"
- "What's on the menu?"
- "Add a Caesar salad to my order"
- "Delivery to 123 Main Street"

**AI will:**
- Present menu options
- Handle customization (extra cheese, etc.)
- Confirm delivery address
- Provide order ID

#### 🏥 HealthCare Plus Hospital (+1-555-HEAL-002)
**Try saying:**
- "I need to book an appointment"
- "I have chest pain"
- "Next Tuesday at 2 PM works"
- "My insurance is BlueCross"

**AI will:**
- Assess medical needs
- Suggest appropriate department
- Check availability
- Collect patient info
- Provide appointment ID

#### 💻 TechFix Support Center (+1-555-TECH-003)
**Try saying:**
- "My WiFi isn't working"
- "I can't install the software"
- "I forgot my password"

**AI will:**
- Diagnose the problem
- Guide through troubleshooting steps
- Offer remote assistance
- Create support ticket

#### ✈️ SkyHigh Travel Agency (+1-555-TRIP-004)
**Try saying:**
- "I want to fly to Paris"
- "Dates are flexible in June"
- "What hotels do you recommend?"
- "I need a window seat"

**AI will:**
- Suggest flight options
- Offer hotel packages
- Handle special requests
- Provide booking reference

#### 📞 Universal Customer Service (+1-555-HELP-005)
**Try saying:**
- "I need to return an item"
- "My order number is ORD-12345"
- "I have a billing question"

**AI will:**
- Handle general inquiries
- Process returns/refunds
- Resolve complaints
- Create service tickets

### 6️⃣ Customization Guide

#### Adding New Services

1. **Edit `app.py`** - Add to `SERVICES` dict:
```python
"newservice": {
    "name": "New Service Name",
    "phone": "+1-555-NEW-006",
    "color": "#FF5733",
    "icon": "🎉",
    "description": "Service description"
}
```

2. **Add Master Prompt** to `MASTER_PROMPTS`:
```python
"newservice": """
You are an AI assistant for New Service.
Your responsibilities:
1. Task one
2. Task two
...
"""
```

3. **Restart the server**

#### Changing AI Voice

In `app.py`, modify voice selection:
```python
voice_name="Kore"  # Professional
voice_name="Puck"  # Friendly
voice_name="Charon"  # Deep
voice_name="Zephyr"  # Warm
```

### 7️⃣ Troubleshooting

#### "API Key Error"
- Make sure GEMINI_API_KEY is set
- Check for typos in the key
- Verify key is active at https://aistudio.google.com

#### "Microphone Not Working"
- Check browser permissions (usually a popup)
- Try different browser (Chrome/Edge recommended)
- Check Windows sound settings
- Use headphones if echo occurs

#### "PyAudio Won't Install"
- Download pre-built wheel (see step 2B above)
- Or skip PyAudio and use text-only demo runner

#### "Port 5000 Already in Use"
- Change port in `app.py`: `socketio.run(app, port=5001)`
- Or close other apps using port 5000

#### "No Audio from AI"
- Check speaker/headphone connection
- Verify volume settings
- Try refreshing the page

### 8️⃣ Performance Tips

- **Use headphones** to prevent echo/feedback
- **Speak clearly** near microphone
- **Wait for AI to finish** before responding
- **Close other audio apps** to prevent conflicts
- **Use Chrome or Edge** for best compatibility

### 9️⃣ Demo Presentation Tips

For client presentations:

1. **Start with the dashboard** showing all 5 services
2. **Explain the use case** for each service
3. **Live call demo** - Pick 2-3 services to demonstrate
4. **Show the data tracking** - Orders, appointments, tickets
5. **Highlight scalability** - Easy to add more services

Talking points:
- "Real-time voice AI, not pre-recorded"
- "Handles complex conversations naturally"
- "Extracts and stores structured data"
- "Scalable to dozens of services"
- "Professional UI ready for production"

### 🔟 Next Steps

#### For Production Deployment:

1. **Security**
   - Change SECRET_KEY
   - Add user authentication
   - Enable HTTPS
   - Rate limiting

2. **Database**
   - Replace in-memory storage with PostgreSQL/MongoDB
   - Add data persistence

3. **Phone Integration**
   - Integrate with Twilio for real phone numbers
   - Add call recording
   - SMS notifications

4. **Monitoring**
   - Add analytics dashboard
   - Error tracking
   - Performance metrics

5. **Scaling**
   - Deploy to cloud (AWS, Azure, GCP)
   - Load balancing
   - Multiple AI instances

---

## 📞 Need Help?

Check out:
- README.md for overview
- test_system.py for testing
- demo_runner.py for text-based demos

**Happy demoing! 🎉**
