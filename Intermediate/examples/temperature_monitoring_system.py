import time
import Adafruit_DHT

# Define sensor type and pin
sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO pin connected to the DHT22 sensor

def get_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.2f} C")
        print(f"Humidity: {humidity:.2f} %")
    else:
        print("Failed to retrieve data from sensor.")

def log_temperature():
    with open("temperature_log.txt", "a") as log_file:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            if humidity is not None and temperature is not None:
                log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Temp: {temperature:.2f} C, Humidity: {humidity:.2f} %\n")
                print(f"Data logged: {temperature:.2f} C, {humidity:.2f} %")
            else:
                print("Failed to retrieve data from sensor.")
            time.sleep(60)  # Log every minute

if __name__ == "__main__":
    log_temperature()
