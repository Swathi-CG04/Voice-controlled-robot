@echo off
echo Voice-Controlled Robotic Arm Simulation Setup
echo ============================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! Please install Python 3.7 or newer.
    exit /b 1
)

echo Installing required Python packages...
pip install -r requirements.txt

echo.
echo Setup completed successfully!
echo.
echo To run the simulation:
echo 1. Install Webots from https://www.cyberbotics.com/
echo 2. Start Webots and open worlds/robotic_arm.wbt
echo 3. Run the voice control script with: python voice_control.py
echo.
echo For debug mode (text commands): python voice_control.py --debug
echo. 