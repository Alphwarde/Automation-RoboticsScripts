#include <NewPing.h>

#define TRIG 9
#define ECHO 10
#define MOTOR_LEFT 5
#define MOTOR_RIGHT 6

NewPing sonar(TRIG, ECHO, 200);

void setup() {
    pinMode(MOTOR_LEFT, OUTPUT);
    pinMode(MOTOR_RIGHT, OUTPUT);
}

void loop() {
    int distance = sonar.ping_cm();
    if (distance > 10 || distance == 0) {
        digitalWrite(MOTOR_LEFT, HIGH);
        digitalWrite(MOTOR_RIGHT, HIGH);
    } else {
        digitalWrite(MOTOR_LEFT, LOW);
        digitalWrite(MOTOR_RIGHT, LOW);
        delay(500);
        digitalWrite(MOTOR_LEFT, HIGH);
        digitalWrite(MOTOR_RIGHT, LOW);
        delay(500);
    }
}
