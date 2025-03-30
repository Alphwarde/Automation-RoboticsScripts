
# **Speech and Gesture Control for Robotics**

## **Overview**
This project allows users to control a robot via speech recognition and hand gestures. It uses a combination of speech-to-text technology and real-time hand tracking to send commands to a microcontroller (such as an Arduino or ESP32) over serial communication. The robot can move forward, backward, left, right, or stop based on voice commands and hand gestures.

---

## **Components**
- **Microcontroller (Arduino/ESP32)**: The core of the robot, responsible for receiving commands and controlling motors.
- **Speech Recognition (via Python)**: Converts voice commands to text and sends corresponding commands to the robot.
- **Gesture Recognition (via OpenCV and MediaPipe)**: Uses hand gestures captured via a webcam to control the robot.
- **Serial Communication (via Python `serial` library)**: Sends control commands from the Python script to the robot over a serial connection.

---

## **Features**
- Voice control for basic robot movements (forward, backward, left, right, and stop).
- Gesture control through hand tracking to manage robot's movement.
- Seamless integration of voice and gesture control for dynamic interaction.
- Real-time feedback for recognized gestures and voice commands.

---

## **How It Works**
1. **Speech Recognition**:
   - The Python script listens for voice commands through the microphone.
   - Voice commands like "forward", "backward", "left", "right", and "stop" are converted into text using Google's speech-to-text API.
   - The corresponding command (e.g., 'F' for forward) is sent to the robot via serial communication.

2. **Gesture Control**:
   - The webcam continuously captures frames, and MediaPipe detects hand landmarks.
   - Specific hand gestures correspond to different movement commands:
     - **Forward**: Index finger pointed up.
     - **Backward**: Palm facing up (thumb pointing down).
     - **Left**: Thumb to the left of the index finger.
     - **Right**: Thumb to the right of the index finger.
     - **Stop**: Fist gesture.
   - Each gesture sends a serial command to the robot to control its movement.

3. **Integration**:
   - The Python script continuously checks for both voice commands and hand gestures. 
   - It runs speech recognition in a separate thread so that both input methods (voice and gesture) can work simultaneously.

---

## **Dependencies**
To run this project, ensure you have the following dependencies installed:

1. **Python 3.x**: The primary language for the script.
2. **SpeechRecognition**: For converting speech to text.
   ```bash
   pip install SpeechRecognition
   ```
3. **PyAudio**: Required for microphone input (install on Linux/Mac using `sudo apt-get install portaudio19-dev` if you face issues).
   ```bash
   pip install pyaudio
   ```
4. **OpenCV**: For computer vision tasks.
   ```bash
   pip install opencv-python
   ```
5. **MediaPipe**: For hand gesture detection.
   ```bash
   pip install mediapipe
   ```
6. **pySerial**: For serial communication with the robot (Arduino/ESP32).
   ```bash
   pip install pyserial
   ```

---

## **How to Use**
1. **Hardware Setup**:
   - Connect your robot's microcontroller (Arduino/ESP32) to your computer via USB.
   - Ensure the microcontroller is programmed to receive and execute serial commands for controlling motors.
   
2. **Running the Script**:
   - Ensure all dependencies are installed.
   - Modify the serial port in the script to match your system's port (e.g., `/dev/ttyUSB0` or `COM3`).
   - Run the Python script. It will start listening for voice commands and hand gestures.
   - Speak a command like "forward", "left", etc., or use hand gestures to control the robot.
   
3. **Stopping the Program**:
   - Press `q` to stop the webcam feed and exit the program.

---

## **Applications**
- **Robotic Automation**: Control robots using voice and gestures for navigation and tasks.
- **Human-Robot Interaction**: A more intuitive way to control robots, especially in environments where traditional controls are inconvenient.
- **Accessibility**: Providing alternate methods for controlling robots for people with disabilities (e.g., voice or gesture-based control).

---

## **Future Improvements**
- Adding more complex gestures or voice commands.
- Implementing obstacle avoidance based on sensor input (e.g., ultrasonic or infrared).
- Expanding control to additional robots or devices.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

