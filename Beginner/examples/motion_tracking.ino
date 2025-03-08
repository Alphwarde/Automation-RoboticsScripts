#include <Servo.h>

Servo tracker;
int sensorPin = A0;
int pos = 90;

void setup() {
    tracker.attach(9);
    pinMode(sensorPin, INPUT);
    tracker.write(pos);
}

void loop() {
    int sensorValue = analogRead(sensorPin);
    if (sensorValue > 500) {
        pos += 5;
    } else {
        pos -= 5;
    }
    pos = constrain(pos, 0, 180);
    tracker.write(pos);
    delay(50);
}
