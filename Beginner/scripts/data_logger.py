# This script reads data from sensors (e.g., temperature sensor) and logs the data to a file.

import time
import random

def get_temperature():
    return random.uniform(20.0, 30.0)

def log_data():
    with open("sensor_log.txt", "a") as f:
        while True:
            sensor_reading = get_data()
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {sensor_reading}C\n")
            time.sleep(5)

if __name__ == "__main__":
    log_data()

# Note that this only works for specific sensors that have 2 outputs like the get_temperature function , change it as you please
