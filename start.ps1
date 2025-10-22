# Quick Start Script for AI Calling Agent Demo
# This script will help you set up and run the system

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 59) -ForegroundColor Cyan
Write-Host "🚀 AI Calling Agent System - Quick Start" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 59) -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "📋 Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python 3.8 or higher" -ForegroundColor Red
    exit 1
}

# Check if API key is set
Write-Host ""
Write-Host "🔑 Checking API key..." -ForegroundColor Yellow
if (-not $env:GEMINI_API_KEY) {
    Write-Host "⚠️  GEMINI_API_KEY not set!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Please enter your Gemini API key:" -ForegroundColor Cyan
    Write-Host "(Get it from: https://aistudio.google.com/app/apikey)" -ForegroundColor Gray
    $apiKey = Read-Host "API Key"
    $env:GEMINI_API_KEY = $apiKey
    Write-Host "✅ API key set for this session" -ForegroundColor Green
} else {
    Write-Host "✅ API key found" -ForegroundColor Green
}

# Install dependencies
Write-Host ""
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "⚠️  Some dependencies may have failed to install" -ForegroundColor Yellow
    Write-Host "Note: PyAudio can be tricky on Windows. If it fails:" -ForegroundColor Gray
    Write-Host "  1. Download from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio" -ForegroundColor Gray
    Write-Host "  2. Install with: pip install PyAudio-X.X.X-cpXX-cpXX-win_amd64.whl" -ForegroundColor Gray
}

# Display system info
Write-Host ""
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 59) -ForegroundColor Cyan
Write-Host "📞 Available Services:" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 59) -ForegroundColor Cyan
Write-Host "🍔 GourmetEats Restaurant    : +1-555-FOOD-001" -ForegroundColor White
Write-Host "🏥 HealthCare Plus Hospital  : +1-555-HEAL-002" -ForegroundColor White
Write-Host "💻 TechFix Support Center    : +1-555-TECH-003" -ForegroundColor White
Write-Host "✈️  SkyHigh Travel Agency     : +1-555-TRIP-004" -ForegroundColor White
Write-Host "📞 Universal Customer Service: +1-555-HELP-005" -ForegroundColor White
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 59) -ForegroundColor Cyan

# Start the server
Write-Host ""
Write-Host "🌐 Starting the dashboard server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "🎯 Dashboard will be available at: http://localhost:5000" -ForegroundColor Green
Write-Host "📝 Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 59) -ForegroundColor Cyan
Write-Host ""

# Start the application
python app.py
