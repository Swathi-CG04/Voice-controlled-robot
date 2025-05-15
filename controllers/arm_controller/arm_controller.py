#!/usr/bin/env python3

"""
Controller for a voice-controlled robotic arm.
"""

from controller import Robot, Motor, PositionSensor
import sys
import socket
import json
import threading
import time

# Initialize the robot controller
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Get motor and position sensor devices
motor1 = robot.getDevice("motor1")
motor2 = robot.getDevice("motor2")
motor3 = robot.getDevice("motor3")
gripper_motor = robot.getDevice("gripper_motor")

position_sensor1 = robot.getDevice("position_sensor1")
position_sensor2 = robot.getDevice("position_sensor2")
position_sensor3 = robot.getDevice("position_sensor3")
gripper_sensor = robot.getDevice("gripper_sensor")

# Enable position sensors
position_sensor1.enable(timestep)
position_sensor2.enable(timestep)
position_sensor3.enable(timestep)
gripper_sensor.enable(timestep)

# Set motors to position control mode
motor1.setPosition(0.0)
motor2.setPosition(0.0)
motor3.setPosition(0.0)
gripper_motor.setPosition(0.0)

# Create a socket server to receive commands from voice recognition script
class CommandServer:
    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.commands = []
        self.command_lock = threading.Lock()
        self.running = True
        
    def start(self):
        self.thread = threading.Thread(target=self.listen_for_commands)
        self.thread.daemon = True
        self.thread.start()
        
    def listen_for_commands(self):
        print("Command server listening on", self.host, "port", self.port)
        while self.running:
            try:
                client, addr = self.socket.accept()
                with client:
                    print('Connected by', addr)
                    data = client.recv(1024)
                    if data:
                        try:
                            command = json.loads(data.decode('utf-8'))
                            with self.command_lock:
                                self.commands.append(command)
                            client.sendall(b'Command received')
                        except json.JSONDecodeError:
                            print("Error: Invalid JSON data received")
                            client.sendall(b'Error: Invalid JSON data')
            except Exception as e:
                if self.running:
                    print("Error in command server:", e)
                    time.sleep(1)  # Prevent rapid reconnection attempts
    
    def get_next_command(self):
        with self.command_lock:
            if self.commands:
                return self.commands.pop(0)
            return None
    
    def stop(self):
        self.running = False
        self.socket.close()

# Start the command server
cmd_server = CommandServer()
cmd_server.start()

# Dictionary of predefined positions
positions = {
    "home": {"motor1": 0.0, "motor2": 0.0, "motor3": 0.0, "gripper": 0.0},
    "up": {"motor1": 0.0, "motor2": -1.57, "motor3": -1.57, "gripper": 0.0},
    "down": {"motor1": 0.0, "motor2": 1.57, "motor3": 1.57, "gripper": 0.0},
    "left": {"motor1": 1.57, "motor2": 0.0, "motor3": 0.0, "gripper": 0.0},
    "right": {"motor1": -1.57, "motor2": 0.0, "motor3": 0.0, "gripper": 0.0},
    "open": {"motor1": None, "motor2": None, "motor3": None, "gripper": 0.5},
    "close": {"motor1": None, "motor2": None, "motor3": None, "gripper": 0.0},
}

# Main control loop
print("Robot controller started")
while robot.step(timestep) != -1:
    # Check for new commands
    command = cmd_server.get_next_command()
    if command:
        print(f"Received command: {command}")
        
        # Handle command
        if 'action' in command:
            action = command['action'].lower()
            
            # Move to predefined position
            if action in positions:
                position = positions[action]
                if position['motor1'] is not None:
                    motor1.setPosition(position['motor1'])
                if position['motor2'] is not None:
                    motor2.setPosition(position['motor2'])
                if position['motor3'] is not None:
                    motor3.setPosition(position['motor3'])
                if position['gripper'] is not None:
                    gripper_motor.setPosition(position['gripper'])
                print(f"Moving to position: {action}")
            
            # Custom positions
            elif action == 'custom':
                if 'motor1' in command:
                    motor1.setPosition(float(command['motor1']))
                if 'motor2' in command:
                    motor2.setPosition(float(command['motor2']))
                if 'motor3' in command:
                    motor3.setPosition(float(command['motor3']))
                if 'gripper' in command:
                    gripper_motor.setPosition(float(command['gripper']))
            
            # Stop the robot
            elif action == 'stop':
                motor1.setVelocity(0)
                motor2.setVelocity(0)
                motor3.setVelocity(0)
                gripper_motor.setVelocity(0)
            
            # Print the current position
            elif action == 'position':
                pos1 = position_sensor1.getValue()
                pos2 = position_sensor2.getValue()
                pos3 = position_sensor3.getValue()
                gripper_pos = gripper_sensor.getValue()
                print(f"Current position: motor1={pos1:.2f}, motor2={pos2:.2f}, motor3={pos3:.2f}, gripper={gripper_pos:.2f}") 