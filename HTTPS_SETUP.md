# 🔒 HTTPS Setup Guide - Fix Microphone Access

## The Problem
Browsers require HTTPS (or localhost) to access the microphone for security reasons. If you're seeing:
- `navigator.mediaDevices is undefined`
- No microphone permission prompt

This means you need to enable HTTPS!

## ✅ Quick Fix - Method 1: Adhoc SSL (Easiest)

### Already Configured! Just restart the server:

```powershell
python app.py
```

The server will now run with HTTPS at: **https://localhost:5000**

### When you open the page:

1. Your browser will show: **"Your connection is not private"** or **"Not Secure"**
2. This is NORMAL for development! Click:
   - **Chrome/Edge**: "Advanced" → "Proceed to localhost (unsafe)"
   - **Firefox**: "Advanced" → "Accept the Risk and Continue"
3. The page will load and microphone access will work! ✅

## 🔐 Method 2: Generate Your Own Certificate (More Persistent)

If you want a certificate that persists between restarts:

### Step 1: Generate Certificate

```powershell
# Install OpenSSL if not already installed
# Download from: https://slproweb.com/products/Win32OpenSSL.html

# Generate certificate (valid for 365 days)
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

You'll be asked for information:
- Country: US
- State: California
- City: San Francisco
- Organization: Your Company
- Common Name: **localhost** (IMPORTANT!)
- Email: your@email.com

### Step 2: Update app.py

Change the last line:
```python
# FROM:
socketio.run(app, debug=True, host='0.0.0.0', port=5000, ssl_context='adhoc')

# TO:
socketio.run(app, debug=True, host='0.0.0.0', port=5000, 
             ssl_context=('cert.pem', 'key.pem'))
```

### Step 3: Restart Server

```powershell
python app.py
```

## 📱 Access Your Applications

Once HTTPS is enabled:

- **Main Dashboard**: https://localhost:5000
- **Phone Dialer**: https://localhost:5000/dialer
- **Microphone Test**: https://localhost:5000/mic-test

## 🎯 For Your Demo

### Best Practice for Client Presentations:

1. **Start the server** with HTTPS enabled
2. **Before the demo**, open https://localhost:5000 in your browser
3. **Accept the certificate warning** once (it won't ask again in that session)
4. **Test the microphone** using the "Test Microphone" button
5. **Now you're ready** for your demo!

## 🔧 Troubleshooting

### Still seeing "mediaDevices is undefined"?

1. **Make sure you're using `https://`** not `http://`
2. **Use `localhost`** not `127.0.0.1` or IP address
3. **Clear browser cache** and reload (Ctrl+Shift+R)
4. **Try a different browser** (Chrome/Edge recommended)

### Certificate errors persist?

```powershell
# Regenerate certificate
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# Make sure Common Name = localhost
```

### Port already in use?

Change the port in app.py:
```python
socketio.run(app, debug=True, host='0.0.0.0', port=5001, ssl_context='adhoc')
```
Then access: https://localhost:5001

## 🌐 Alternative: Using ngrok (For Remote Demos)

If you need to demo over the internet:

```powershell
# Install ngrok: https://ngrok.com/download

# Start your server normally (HTTP is fine)
python app.py

# In another terminal:
ngrok http 5000
```

Ngrok provides a secure HTTPS URL automatically! Share that URL for remote demos.

## ✅ Verification Checklist

- [ ] PyOpenSSL installed (`pip install pyopenssl`)
- [ ] Server running with HTTPS
- [ ] Accessing via https://localhost:5000
- [ ] Certificate warning accepted in browser
- [ ] Microphone test button shows "✅ Microphone access granted!"
- [ ] Can see service cards and dialer
- [ ] Ready to make calls!

## 📝 Quick Commands

```powershell
# Install SSL support
pip install pyopenssl

# Start server with HTTPS
python app.py

# Open in browser (accept certificate warning)
start https://localhost:5000

# Test microphone
# Click "Test Microphone" button on dashboard
```

## 🎉 You're All Set!

Once HTTPS is working, your microphone access will work perfectly for:
- ✅ Dashboard calls
- ✅ Phone dialer
- ✅ All 5 AI services
- ✅ Live transcription
- ✅ Real-time audio streaming

**Important**: The certificate warning is normal for development. For production, you would use a real certificate from Let's Encrypt or a trusted CA.

---

**Need more help?** Check:
- `QUICKSTART.md` for general setup
- `SETUP_GUIDE.md` for detailed installation
- `README.md` for project overview
