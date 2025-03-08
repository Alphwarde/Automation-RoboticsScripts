# Autonomous Robot Navigation

## Overview
This project focuses on creating an autonomous robot that can navigate a room and avoid obstacles using ultrasonic sensors. The robot will be able to detect objects in its path and automatically adjust its course to avoid collisions.

## Components
- **Ultrasonic Sensor**: Used to measure the distance between the robot and obstacles.
- **Motors**: Controls the movement of the robot.
- **Microcontroller (Arduino)**: Used for processing sensor data and controlling the robot's motors.

## Features
- Navigation using ultrasonic sensors for obstacle avoidance.
- Ability to navigate a pre-defined path while avoiding obstacles.

## How It Works
1. The ultrasonic sensor continuously measures the distance to the nearest object in front of the robot.
2. The robot moves forward until an obstacle is detected within a defined distance threshold.
3. When an obstacle is detected, the robot turns to avoid the object.
4. The process repeats, enabling the robot to navigate around the room.

## Applications
- Autonomous navigation in indoor environments.
- Can be used in robot competitions or educational projects to demonstrate navigation and sensor integration.
