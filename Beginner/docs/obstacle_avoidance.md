# Obstacle Avoidance

This example demonstrates how to use sensors to help a robot avoid obstacles.

### Components Used:
- Ultrasonic sensor
- DC motors
- Arduino board

### How it works:
- The ultrasonic sensor measures the distance to an obstacle.
- The robot adjusts its movement to avoid obstacles based on sensor readings.

### Code Example:
```cpp
const int trigPin = 9;
const int echoPin = 10;
const int motor1 = 6;
const int motor2 = 5;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motor1, OUTPUT);
  pinMode(motor2, OUTPUT);
}

void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.0344 / 2;

  if (distance < 10) {
    digitalWrite(motor1, LOW);
    digitalWrite(motor2, HIGH);
  } else {
    digitalWrite(motor1, HIGH);
    digitalWrite(motor2, HIGH);
  }
  delay(100);
}
