# Motion Tracking

This example demonstrates how to use sensors and motors to track motion.

### Components Used:
- Servo motor
- Ultrasonic sensor
- Arduino board

### How it works:
- The ultrasonic sensor detects distance and adjusts the position of the servo motor based on the distance.
- The code uses a simple mapping function to convert the distance into an angle for the servo.

### Code Example:
```cpp
#include <Servo.h>

Servo motor;
int trigPin = 9;
int echoPin = 10;
long duration, distance;

void setup() {
  motor.attach(6);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.0344 / 2;

  int angle = map(distance, 0, 200, 0, 180);
  motor.write(angle);
  delay(500);
}
