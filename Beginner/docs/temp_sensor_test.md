
# Temperature Sensor Test

This example demonstrates how to read the temperature using a sensor like the LM35 and display it on the serial monitor.

### Components Used:
- LM35 temperature sensor
- Arduino board

### How it works:
- The LM35 sensor gives an analog output that corresponds to the temperature.
- The code reads the sensor's value and converts it to Celsius.

### Code Example:
```cpp
int sensorPin = A0;
float tempC;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  tempC = (sensorValue * 5.0 * 100.0) / 1024.0;
  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println(" C");
  delay(1000);
}
