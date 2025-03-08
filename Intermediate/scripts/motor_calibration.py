import time
import random

def calibrate_motor(motor_id):
    """Simulate motor calibration."""
    print(f"Calibrating motor {motor_id}...")
    for speed in range(0, 255, 50):  # Run the motor through speed cycles
        print(f"Setting motor {motor_id} speed to {speed}")
        time.sleep(1)
    print(f"Motor {motor_id} calibration complete.")

def main():
    motors = [1, 2]  # Example motor IDs
    for motor in motors:
        calibrate_motor(motor)

if __name__ == "__main__":
    main()
