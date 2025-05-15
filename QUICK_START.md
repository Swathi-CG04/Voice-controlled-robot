# Quick Start Guide

This guide provides quick step-by-step instructions to get your voice-controlled robotic arm simulation up and running.

## Windows Users

1. **Install Webots**
   - Download from: https://www.cyberbotics.com/download
   - Follow the installation wizard instructions

2. **Install Python and dependencies**
   - Make sure Python 3.7+ is installed
   - Run `setup.bat` to install required packages
   - Alternatively, run: `pip install -r requirements.txt`

3. **Start the simulation**
   - Run Webots and open the file: `worlds/robotic_arm.wbt`
   - Wait for the simulation to load
   - Click the play button in Webots to start the simulation

4. **Start voice control**
   - Open Command Prompt or PowerShell
   - Run: `python voice_control.py`
   - Alternatively, for text input mode: `python voice_control.py --debug`

5. **Use voice commands**
   - Say any of the supported commands: "home", "up", "down", "left", "right", "open", "close", "stop", "position"
   - The robotic arm should respond to your commands

## WSL Users

1. **Install Webots in Windows**
   - Download from: https://www.cyberbotics.com/download
   - Install in Windows (not in WSL)

2. **Setup WSL environment**
   - Run `setup_wsl.sh` from within WSL: `bash setup_wsl.sh`
   - This will install the required Python packages

3. **Start the simulation**
   - Run Webots from Windows and open the file: `worlds/robotic_arm.wbt`
   - Make sure this file is accessible from Windows
   - Click the play button in Webots to start the simulation

4. **Start voice control from WSL**
   - Run: `python3 voice_control.py`
   - For text input mode: `python3 voice_control.py --debug`
   - The script will automatically detect WSL and use Windows APIs for audio

5. **Use voice commands**
   - When prompted, speak one of the supported commands
   - Commands will be sent to the simulation

## Troubleshooting

- **Webots can't find controller**: Make sure the controller path is correct in Webots
- **Voice recognition not working**: Try the debug mode with `--debug` flag
- **WSL audio issues**: Make sure Windows can access your microphone and WSL integration is enabled

## Next Steps

- Customize the arm behavior by editing `controllers/arm_controller/arm_controller.py`
- Add new voice commands by modifying the `VALID_COMMANDS` list in `voice_control.py`
- Experiment with the robotic arm design in Webots 