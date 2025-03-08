import random
import time

def read_battery_voltage():
    """Simulate battery voltage reading."""
    voltage = random.uniform(3.0, 4.2)  # Simulate a 3.0V to 4.2V range
    return voltage

def log_voltage(voltage):
    """Log voltage to console or file."""
    with open("battery_log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {voltage:.2f}V\n")
        print(f"Voltage: {voltage:.2f}V logged.")

def main():
    while True:
        voltage = read_battery_voltage()
        log_voltage(voltage)
        time.sleep(5)  # Log every 5 seconds

if __name__ == "__main__":
    main()
