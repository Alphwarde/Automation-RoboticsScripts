# Auto Motor Calibration

## Description

The **Motor Calibration** script simulates the process of calibrating motors by running them through a set of predefined speed cycles. It ensures that the motor responds correctly at each speed level, allowing for accurate control in robotics projects.

### Features:
- Simulates motor calibration by running the motor at different speed levels.
- Ensures that motors are calibrated to run at full speed and consistent behavior.
- Useful for robotic motor tuning and performance optimization.

## How It Works

1. The script iterates over a list of motors (in this case, two motors with IDs 1 and 2).
2. It runs each motor through different speed levels (from 0 to 255).
3. For each speed cycle, the motor is run for 1 second to simulate the calibration process.

## Dependencies
- Python 3.x

## How to Use
1. Clone this repository or download the script.
2. Run the script using `python auto_motor_calibration.py`.
3. Watch the console output as the motors are calibrated.

## Example Output

```text
Calibrating motor 1...
Setting motor 1 speed to 0
Setting motor 1 speed to 50
Setting motor 1 speed to 100
Setting motor 1 speed to 150
Setting motor 1 speed to 200
Setting motor 1 speed to 250
Motor 1 calibration complete.

Calibrating motor 2...
Setting motor 2 speed to 0
Setting motor 2 speed to 50
Setting motor 2 speed to 100
Setting motor 2 speed to 150
Setting motor 2 speed to 200
Setting motor 2 speed to 250
Motor 2 calibration complete.
