# Voice-Controlled Robotic Arm Simulation

This project implements a voice-controlled robotic arm simulation using Webots and Python. It's designed to work with both standard Windows and WSL environments.

## Prerequisites

1. **Webots**: Download and install Webots from [https://www.cyberbotics.com/](https://www.cyberbotics.com/)
2. **Python 3.7+**: Make sure you have Python installed
3. **Required Python packages**:
   ```
   pip install SpeechRecognition PyAudio
   ```
   Note: Installing PyAudio can be challenging on some systems:
   - Windows: You might need Microsoft Visual C++ 14.0 or greater
   - Linux/WSL: `sudo apt-get install python3-pyaudio`

## Project Structure

- `worlds/robotic_arm.wbt` - Webots world file with robotic arm model
- `controllers/arm_controller/arm_controller.py` - Robot controller for Webots
- `voice_control.py` - Voice recognition script that sends commands to the robot

## Setup

1. **Install Webots**: Follow the instructions for your operating system at [https://www.cyberbotics.com/download](https://www.cyberbotics.com/download)

2. **Install Python dependencies**:
   ```
   pip install SpeechRecognition PyAudio
   ```

3. **WSL-specific setup**:
   If you're using WSL, you'll need to ensure you can access the Windows audio system:
   - The script handles WSL detection automatically
   - It uses PowerShell commands via `subprocess` to access Windows audio
   - No additional setup is required, but you need to run WSL with Windows integration

## Running the Simulation

1. **Start Webots and open the simulation**:
   ```
   webots worlds/robotic_arm.wbt
   ```

2. **Start the voice recognition script**:
   ```
   python voice_control.py
   ```
   
   Or for debug mode (text input instead of voice):
   ```
   python voice_control.py --debug
   ```

## Voice Commands

The simulation recognizes the following commands:

- `home` - Move the arm to the home position
- `up` - Move the arm upward
- `down` - Move the arm downward
- `left` - Move the arm to the left
- `right` - Move the arm to the right
- `open` - Open the gripper
- `close` - Close the gripper
- `stop` - Stop all motors
- `position` - Print the current position of all motors

## Troubleshooting

1. **Voice recognition issues**:
   - Make sure your microphone is working properly
   - Try speaking more clearly and directly into the microphone
   - If using WSL, ensure Windows can access your microphone

2. **Connection issues**:
   - Make sure Webots is running with the robotic arm simulation
   - Verify that the controller is properly loaded in Webots
   - Check if port 65432 is available (you can change the port in the voice_control.py script)

3. **WSL-specific issues**:
   - Ensure WSL has integration with Windows enabled
   - Try running the script with `--debug` flag to test with text input
   - Make sure PowerShell commands can be executed from WSL

## Customization

- Add new commands by updating the `VALID_COMMANDS` list in `voice_control.py`
- Define new positions by updating the `positions` dictionary in `arm_controller.py`
- Modify the robotic arm design by editing the `robotic_arm.wbt` file in Webots 