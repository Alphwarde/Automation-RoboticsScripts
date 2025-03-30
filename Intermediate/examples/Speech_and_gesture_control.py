import cv2
import mediapipe as mp
import serial
import speech_recognition as sr
import threading
# Ill try to explain the moves to do infront of the camera as much as i can so bear with me :)
# Set up serial communication (adjust port to your ESP32 or Arduino)
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Command mappings for both speech and gestures
commands = {
    "forward": "F",  # Voice command 'forward' sends 'F' to the robot
    "backward": "B",
    "left": "L",
    "right": "R",
    "stop": "S"
}

# Speech recognition setup
recognizer = sr.Recognizer()  # Initialize speech recognizer

# MediaPipe hand tracking setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)  # Use the default camera

# Function to handle speech recognition in a separate thread
def listen_for_speech():
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

# Start the speech recognition in a separate thread
speech_thread = threading.Thread(target=listen_for_speech)
speech_thread.daemon = True  # Make sure it terminates when the program ends
speech_thread.start()

# Loop to continuously capture video frames and detect hand gestures
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)  # Flip the frame for easier mirror view
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for MediaPipe
    results = hands.process(rgb_frame)  # Process the frame to detect hands

    if results.multi_hand_landmarks:  # Check if hands are detected
        for landmarks in results.multi_hand_landmarks:
            # Getting positions of key landmarks for gesture detection
            index_tip = landmarks.landmark[8]  # Index finger tip
            thumb_tip = landmarks.landmark[4]  # Thumb tip
            thumb_base = landmarks.landmark[2]  # Thumb base
            middle_finger = landmarks.landmark[12]  # Middle finger tip

            # Forward gesture: Index finger up
            if index_tip.y < landmarks.landmark[6].y:  # Index tip above knuckle
                ser.write(b'F')  # Send forward command
            # Backward gesture: Palm facing up (thumb facing down)
            elif thumb_tip.y > middle_finger.y:  # Thumb tip is lower than middle finger
                ser.write(b'B')  # Send backward command
            # Left gesture: Thumb left of index (palm facing forward)
            elif thumb_tip.x < index_tip.x:  # Thumb is to the left of index
                ser.write(b'L')  # Send left command
            # Right gesture: Thumb right of index (palm facing forward)
            elif thumb_tip.x > index_tip.x:  # Thumb is to the right of index
                ser.write(b'R')  # Send right command
            # Stop gesture: All fingers curled (fist)
            elif (index_tip.y > landmarks.landmark[7].y and  # Index curled
                  landmarks.landmark[6].y > landmarks.landmark[7].y and  # Hand closed
                  thumb_base.x < thumb_tip.x):  # Thumb curled
                ser.write(b'S')  # Send stop command

    # Show the webcam frame with gesture annotations
    cv2.imshow("Gesture Control", frame)

    # Exit when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up after the loop ends
cap.release()
cv2.destroyAllWindows()
