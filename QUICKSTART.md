# 🎯 QUICK START GUIDE - AI Calling Agent Demo

## ⚡ 3-Step Setup

### 1. Install & Configure
```powershell
# Set your API key (get from: https://aistudio.google.com/app/apikey)
$env:GEMINI_API_KEY = "your-api-key"

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch
```powershell
# Option A: Quick start script
.\start.ps1

# Option B: Direct run
python app.py
```

### 3. Use
Open browser → http://localhost:5000 → Click service → Call Now!

---

## 📞 The 5 Services

| Service | Phone Number | What It Does |
|---------|-------------|--------------|
| 🍔 **Restaurant** | +1-555-FOOD-001 | Takes food orders, handles delivery |
| 🏥 **Hospital** | +1-555-HEAL-002 | Books medical appointments |
| 💻 **Tech Support** | +1-555-TECH-003 | Troubleshoots technical issues |
| ✈️ **Travel Agency** | +1-555-TRIP-004 | Books flights and hotels |
| 📞 **Customer Service** | +1-555-HELP-005 | General inquiries and support |

---

## 🎬 Demo Tips

### For Client Presentations:

1. **Start with overview page** (templates/index.html)
2. **Show the dashboard** - All 5 services displayed
3. **Live demo** - Call restaurant or hospital
4. **Show data tracking** - Orders/appointments tabs
5. **Emphasize**:
   - Real-time voice AI (not pre-recorded)
   - Automatic data extraction
   - Easy to scale (add more services)
   - Production-ready UI

### Sample Conversations:

**Restaurant** 🍔
- "I'd like to order a large pizza"
- "Add extra cheese please"
- "Delivery to 123 Main Street"

**Hospital** 🏥
- "I need to book an appointment"
- "I have chest pain occasionally"
- "Tuesday at 2 PM works for me"

**Tech Support** 💻
- "My WiFi isn't connecting"
- "I restarted the router already"
- "Windows 11, Dell laptop"

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| **API Key Error** | Check `$env:GEMINI_API_KEY` is set correctly |
| **Microphone Not Working** | Allow browser permissions, use Chrome/Edge |
| **PyAudio Won't Install** | Download wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio |
| **Port 5000 In Use** | Change port in app.py line: `socketio.run(app, port=5001)` |
| **No Audio Output** | Check speakers, refresh page, try headphones |

---

## 📁 Key Files

- `app.py` - Main server (add services here)
- `templates/dashboard.html` - Main UI
- `templates/index.html` - Overview/landing page
- `demo_runner.py` - Test conversations without voice
- `test_system.py` - Verify system is working
- `SETUP_GUIDE.md` - Detailed installation guide

---

## 🔧 Customize

### Add a New Service:

**Edit app.py**, add to `SERVICES`:
```python
"pharmacy": {
    "name": "HealthMart Pharmacy",
    "phone": "+1-555-DRUG-006",
    "color": "#9B59B6",
    "icon": "💊",
    "description": "Prescription refills"
}
```

Add to `MASTER_PROMPTS`:
```python
"pharmacy": """
You are a pharmacy assistant.
Help customers with prescriptions, refills, etc.
"""
```

Restart server → New service appears!

---

## 📊 Dashboard Features

- **Live Stats**: Total calls, active calls, orders, appointments
- **Service Cards**: Click to call any service
- **Call Modal**: Real-time conversation window
- **Transcript View**: See conversation as it happens
- **Data Tabs**: View collected data (orders, appointments, tickets)

---

## 🎯 What Makes This Demo Special

✅ **Real voice AI** - Not text-to-speech, actual conversational AI
✅ **5 complete services** - Each fully functional with unique behavior
✅ **Live transcription** - See conversations in real-time
✅ **Data extraction** - Automatically captures order IDs, ticket numbers
✅ **Professional UI** - Client-ready design
✅ **Easy to scale** - Add unlimited services
✅ **Production patterns** - Real websockets, async processing

---

## 🚀 Commands Cheat Sheet

```powershell
# Set API key (every new session)
$env:GEMINI_API_KEY = "your-key"

# Quick start
.\start.ps1

# Manual start
python app.py

# Test APIs
python test_system.py

# Demo conversations (text-only)
python demo_runner.py
python demo_runner.py restaurant

# Install missing dependency
pip install package-name
```

---

## 💡 Best Practices

1. **Use headphones** during calls (prevents echo)
2. **Speak clearly** and wait for AI to finish
3. **Chrome/Edge** work best for WebRTC
4. **Close background audio apps** if issues occur
5. **Test before presentation** - Run demo_runner.py first

---

## 📞 Support

Check these files for more details:
- `README.md` - Project overview
- `SETUP_GUIDE.md` - Detailed setup instructions
- Comments in `app.py` - Code documentation

---

**Ready to impress your clients! 🎉**

Dashboard: http://localhost:5000
