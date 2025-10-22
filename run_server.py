"""
Simple launcher for the AI Calling Agent Demo
Checks for API key and starts the server
"""

import os
import sys

print("=" * 70)
print("🚀 AI Calling Agent System - Starting...")
print("=" * 70)

# Check for API key
if not os.environ.get("GEMINI_API_KEY"):
    print("\n⚠️  WARNING: GEMINI_API_KEY environment variable not set!")
    print("\nTo set it, run this in PowerShell:")
    print('$env:GEMINI_API_KEY = "your-api-key-here"')
    print("\nGet your API key from: https://aistudio.google.com/app/apikey")
    print("\n" + "=" * 70)
    
    response = input("\nDo you want to enter the API key now? (y/n): ").strip().lower()
    
    if response == 'y':
        api_key = input("\nEnter your Gemini API Key: ").strip()
        if api_key:
            os.environ["GEMINI_API_KEY"] = api_key
            print("✅ API key set for this session!")
        else:
            print("❌ No API key entered. Exiting...")
            sys.exit(1)
    else:
        print("\n❌ Cannot start without API key. Exiting...")
        sys.exit(1)
else:
    print("✅ API key found!")

print("\n📞 Available Services:")
print("  🍔 GourmetEats Restaurant    : +1-555-FOOD-001")
print("  🏥 HealthCare Plus Hospital  : +1-555-HEAL-002")
print("  💻 TechFix Support Center    : +1-555-TECH-003")
print("  ✈️  SkyHigh Travel Agency     : +1-555-TRIP-004")
print("  📞 Universal Customer Service: +1-555-HELP-005")

print("\n" + "=" * 70)
print("🌐 Dashboard will be available at: http://localhost:5000")
print("📝 Press Ctrl+C to stop the server")
print("=" * 70)
print("\n")

# Import and run the app
try:
    from app import socketio, app
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
except KeyboardInterrupt:
    print("\n\n✅ Server stopped. Goodbye!")
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nMake sure all dependencies are installed:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
