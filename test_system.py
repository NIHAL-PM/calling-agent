# Test script to verify all services
import requests
import time

BASE_URL = "http://localhost:5000"

def test_api_endpoints():
    """Test all API endpoints"""
    print("=" * 60)
    print("🧪 Testing API Endpoints")
    print("=" * 60)
    
    endpoints = [
        "/api/services",
        "/api/stats",
        "/api/call-logs",
        "/api/orders",
        "/api/appointments",
        "/api/tickets"
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            print(f"✅ {endpoint}: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Data: {len(data) if isinstance(data, list) else 'dict'} items")
        except Exception as e:
            print(f"❌ {endpoint}: {str(e)}")
    
    print("=" * 60)

def display_services():
    """Display all available services"""
    print("\n📞 Available Services:")
    print("=" * 60)
    
    try:
        response = requests.get(f"{BASE_URL}/api/services")
        services = response.json()
        
        for key, service in services.items():
            print(f"\n{service['icon']} {service['name']}")
            print(f"   Phone: {service['phone']}")
            print(f"   Description: {service['description']}")
            print(f"   Color: {service['color']}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("=" * 60)

if __name__ == "__main__":
    print("\n🚀 AI Calling Agent System - Test Suite\n")
    
    input("Press Enter to start testing (make sure the server is running)...")
    
    test_api_endpoints()
    display_services()
    
    print("\n✨ Testing complete!")
    print("Open http://localhost:5000 in your browser to see the dashboard")
