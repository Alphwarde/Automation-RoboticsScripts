import speech_recognition as sr
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the port to your ESP32 or Arduino

commands = {
    "forward": "F",  # Voice command 'forward' sends 'F' to the robot
    "backward": "B",
    "left": "L",
    "right": "R",
    "stop": "S"
}

recognizer = sr.Recognizer()  # Initialize speech recognizer

while True:
    with sr.Microphone() as source:
        print("Say command:")
        audio = recognizer.listen(source)  # Listen to microphone input
    
    try:
        # Recognize speech and convert to text
        text = recognizer.recognize_google(audio).lower()  # Use Google's speech-to-text
        print(f"Recognized: {text}")
        if text in commands:
            ser.write(commands[text].encode())  # Send corresponding command to robot (via serial)
    except sr.UnknownValueError:
        print("Could not understand.")
    except sr.RequestError:
        print("Speech service unavailable.")
