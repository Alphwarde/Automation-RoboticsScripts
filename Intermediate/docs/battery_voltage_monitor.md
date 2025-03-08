# Battery Voltage Monitoring

## Description

This script monitors the battery voltage of a device in real-time, logs the voltage readings, and tracks battery health over time. It simulates reading the voltage from a battery and writes the data to a file, allowing users to keep track of the battery's performance and charge level.

### Features:
- Simulates battery voltage readings in the range of 3.0V to 4.2V.
- Logs the voltage readings to a text file with a timestamp.
- Useful for tracking battery health and consumption in robotics or IoT devices.

## How It Works

1. The script generates a simulated battery voltage value between 3.0V and 4.2V.
2. Every 5 seconds, it logs the voltage value to a file `battery_log.txt`, along with the current timestamp.
3. The log file can be used for analyzing battery usage and health over time.

## Dependencies
- Python 3.x

## How to Use
1. Clone this repository or download the script.
2. Run the script using `python battery_voltage_monitor.py`.
3. Check the `battery_log.txt` file to see the voltage log.

## Example Output

```text
2025-03-08 14:12:35: 3.85V
2025-03-08 14:12:40: 4.10V
2025-03-08 14:12:45: 3.75V
