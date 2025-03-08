#include <IRremote.h>

int recv_pin = 7;
IRrecv irrecv(recv_pin);
decode_results results;

int relayPin = 3; // Connect relay module to pin 3

void setup() {
  pinMode(relayPin, OUTPUT);
  irrecv.enableIRIn(); // Start the IR receiver
  Serial.begin(9600);
}

void loop() {
  if (irrecv.decode(&results)) {
    long int decCode = results.value;
    Serial.println(decCode);
    irrecv.resume(); // Receive the next value

    if (decCode == 16724175) {  // Example IR code for ON
      digitalWrite(relayPin, HIGH); // Turn on device
    } else if (decCode == 16718055) {  // Example IR code for OFF
      digitalWrite(relayPin, LOW); // Turn off device
    }
  }
}
