# Data Sync

## Description

The **Data Sync** script simulates the process of syncing sensor data to a remote server. It can be useful for IoT projects where data from sensors or robots needs to be uploaded to a cloud service or remote server.

### Features:
- Simulates sensor data (e.g., temperature and humidity).
- Sends the data to a server (simulated by printing it to the console).
- Useful for IoT projects that require cloud data syncing or remote server communication.

## How It Works

1. The script generates simulated data for temperature and humidity.
2. The data is "sent" to a remote server, which is currently simulated by printing the data to the console.
3. The script loops and syncs the data every 10 seconds.

## Dependencies
- Python 3.x
- `requests` module (optional if you use real server communication)

## How to Use
1. Clone this repository or download the script.
2. Run the script using `python data_sync.py`.
3. Monitor the console output to see the simulated data being sent to the server.

## Example Output

```text
Sending data to server: {'temperature': 24.78, 'humidity': 49.32}
Sending data to server: {'temperature': 25.15, 'humidity': 48.78}
Sending data to server: {'temperature': 23.92, 'humidity': 50.03}
