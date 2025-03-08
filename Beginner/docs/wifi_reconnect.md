
#### 5. **wifi_reconnect.md**

```markdown
# WiFi Reconnect

This example demonstrates how to reconnect to WiFi if the connection is lost.

### Components Used:
- ESP8266 or ESP32 board

### How it works:
- The board tries to connect to a predefined WiFi network.
- If the connection is lost, the code attempts to reconnect.

### Code Example:
```cpp
#include <ESP8266WiFi.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Lost WiFi connection. Reconnecting...");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
    }
    Serial.println("Reconnected to WiFi");
  }
  delay(5000);
}
