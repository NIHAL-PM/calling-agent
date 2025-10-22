@echo off
echo ============================================================
echo       AI Calling Agent System - Quick Start
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found! Please install Python 3.8+
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Check API key
if "%GEMINI_API_KEY%"=="" (
    echo [WARNING] GEMINI_API_KEY not set!
    echo.
    echo Please enter your Gemini API key:
    echo Get it from: https://aistudio.google.com/app/apikey
    set /p GEMINI_API_KEY="API Key: "
)

echo [OK] API key configured
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Display info
echo ============================================================
echo  Available Services:
echo ============================================================
echo  1. GourmetEats Restaurant    : +1-555-FOOD-001
echo  2. HealthCare Plus Hospital  : +1-555-HEAL-002
echo  3. TechFix Support Center    : +1-555-TECH-003
echo  4. SkyHigh Travel Agency     : +1-555-TRIP-004
echo  5. Universal Customer Service: +1-555-HELP-005
echo ============================================================
echo.
echo Starting dashboard at http://localhost:5000
echo Press Ctrl+C to stop
echo.

REM Start the app
python app.py
