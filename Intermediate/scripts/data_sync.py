import random
import time
import requests

def simulate_data():
    """Simulate data from a sensor."""
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(40.0, 60.0)
    return {"temperature": temperature, "humidity": humidity}

def send_to_server(data):
    """Simulate sending data to a remote server."""
    # In a real scenario, replace with a POST request to an API
    print(f"Sending data to server: {data}")

def main():
    while True:
        data = simulate_data()
        send_to_server(data)
        time.sleep(10)  # Sync data every 10 seconds

if __name__ == "__main__":
    main()
