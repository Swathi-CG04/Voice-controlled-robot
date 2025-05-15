#!/bin/bash

echo "Voice-Controlled Robotic Arm Simulation Setup for WSL"
echo "===================================================="

# Check if running in WSL
if ! grep -q Microsoft /proc/version; then
    echo "This script is intended to be run in Windows Subsystem for Linux (WSL)"
    echo "If you're on native Linux, you can install the dependencies directly."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed! Please install Python 3.7 or newer."
    exit 1
fi

# Install dependencies
echo "Installing required Python packages..."
pip3 install SpeechRecognition

# Note about PyAudio
echo
echo "Note about PyAudio:"
echo "PyAudio is not required when running in WSL mode as we'll use Windows"
echo "audio capture through PowerShell."
echo

echo "Setup completed successfully!"
echo
echo "To run the simulation:"
echo "1. Install Webots in Windows from https://www.cyberbotics.com/"
echo "2. Make sure you have the project directory accessible from Windows"
echo "3. Start Webots and open worlds/robotic_arm.wbt"
echo "4. Run the voice control script with: python3 voice_control.py"
echo
echo "For debug mode (text commands): python3 voice_control.py --debug"
echo
echo "Note for WSL users:"
echo "  - Make sure WSL integration with Windows is enabled"
echo "  - Make sure Windows can access your microphone"
echo "  - The script will automatically detect WSL and use Windows audio APIs"
echo 