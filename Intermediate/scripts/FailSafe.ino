#include <Wire.h>

#define MOTOR_PIN 9                 
#define CURRENT_SENSOR A0           
#define ULTRASONIC_TRIGGER 6       
#define ULTRASONIC_ECHO 7          
#define SIGNAL_TIMEOUT 5000         // Signal timeout in milliseconds (5 seconds)

unsigned long lastSignalTime = 0;  
float maxCurrent = 2.0;            // Max current threshold for motor stall (in amp)

void setup() {
    pinMode(MOTOR_PIN, OUTPUT);   
    pinMode(ULTRASONIC_TRIGGER, OUTPUT); 
    pinMode(ULTRASONIC_ECHO, INPUT);   
    Serial.begin(9600);           
}

void loop() {
    // Check motor stall condition (if current exceeds threshold)
    float current = analogRead(CURRENT_SENSOR) * (5.0 / 1023.0);  // Read current (analog)
    if (current > maxCurrent) {
        Serial.println("Motor stall detected,Stopping...");
        digitalWrite(MOTOR_PIN, LOW);  // Stop the motor
    }

    // Check sensor failure (ultrasonic sensor not responding)
    digitalWrite(ULTRASONIC_TRIGGER, LOW);
    delayMicroseconds(2);
    digitalWrite(ULTRASONIC_TRIGGER, HIGH); // Send trigger pulse
    delayMicroseconds(10);
    digitalWrite(ULTRASONIC_TRIGGER, LOW);  // End pulse
    long duration = pulseIn(ULTRASONIC_ECHO, HIGH);  // Measure pulse duration
    if (duration == 0) {
        Serial.println("Sensor failure detected!");
    }

    // Check if the signal was lost (communication timeout)
    if (millis() - lastSignalTime > SIGNAL_TIMEOUT) {
        Serial.println("Signal lost! Stopping...");
        digitalWrite(MOTOR_PIN, LOW);  // Stop if signal is lost
    }
}

// Call this function when a signal is received from the remote (e.g., via Bluetooth)
void updateSignal() {
    lastSignalTime = millis();  // Reset signal timeout counter
}
