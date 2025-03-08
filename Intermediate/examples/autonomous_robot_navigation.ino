#include <NewPing.h>

#define TRIGGER_PIN  12
#define ECHO_PIN     11
#define MAX_DISTANCE 200

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
int motorPinLeft = 6;
int motorPinRight = 5;

void setup() {
  pinMode(motorPinLeft, OUTPUT);
  pinMode(motorPinRight, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  delay(50); 
  int distance = sonar.ping_cm();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance > 15 || distance == 0) { 
    moveForward();
  } else {
    avoidObstacle();
  }
}

void moveForward() {
  digitalWrite(motorPinLeft, HIGH);
  digitalWrite(motorPinRight, HIGH);
}

void avoidObstacle() {
  digitalWrite(motorPinLeft, LOW);
  digitalWrite(motorPinRight, LOW);
  delay(1000);
  turnRight();
}

void turnRight() {
  digitalWrite(motorPinLeft, HIGH);
  digitalWrite(motorPinRight, LOW);
  delay(500);
}
