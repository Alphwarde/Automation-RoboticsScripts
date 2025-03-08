import serial
import time

# Replace '/dev/rfcomm0' with your Bluetooth serial port.
# On Windows, it could be something like 'COMx' (e.g., COM3).
bluetooth_port = '/dev/rfcomm0'  # Bluetooth serial port
baud_rate = 9600               


bluetooth = serial.Serial(bluetooth_port, baud_rate)
time.sleep(2)  # Wait for the connection to establish

def send_command(command):  
    bluetooth.write(command.encode())
    print(f"Sent command: {command}")

def main():

    print("Bluetooth Controller for Robot")
    print("Commands: F = Forward, B = Backward, L = Left, R = Right, S = Stop")
    
    while True:
        command = input("Enter command (F/B/L/R/S): ").upper()
        
        if command in ['F', 'B', 'L', 'R', 'S']:
            send_command(command)
        else:
            print("Invalid command. Use F, B, L, R, or S.")
        
        if command == 'S':
            print("Stopping controller.")
            break

   
    bluetooth.close()

if __name__ == "__main__":
    main()
