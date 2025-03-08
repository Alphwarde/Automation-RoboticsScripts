#include <AFMotor.h>
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX, TX for Bluetooth communication

AF_DCMotor motorLeft(1); // Motor A
AF_DCMotor motorRight(2); // Motor B

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);  // Start Bluetooth communication
  motorLeft.setSpeed(255);  // Set motor speed (max)
  motorRight.setSpeed(255); // Set motor speed (max)
}

void loop() {
  if (BTSerial.available()) {
    char command = BTSerial.read();

    if (command == 'F') { // Move forward
      motorLeft.forward();
      motorRight.forward();
    }
    else if (command == 'B') { // Move backward
      motorLeft.backward();
      motorRight.backward();
    }
    else if (command == 'L') { // Turn left
      motorLeft.backward();
      motorRight.forward();
    }
    else if (command == 'R') { // Turn right
      motorLeft.forward();
      motorRight.backward();
    }
    else if (command == 'S') { // Stop
      motorLeft.setSpeed(0);
      motorRight.setSpeed(0);
    }
  }
}
