#include <DHT.h>
#include <ESP8266WiFi.h>

#define DHTPIN 2          // Pin for DHT sensor
#define DHTTYPE DHT22     // DHT 22 (AM2302)
#define WIFI_SSID "your_wifi_ssid"
#define WIFI_PASSWORD "your_wifi_password"
#define SERVER "your.server.com" // Example server for uploading data

DHT dht(DHTPIN, DHTTYPE);

WiFiClient client;

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectToWiFi();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int lightLevel = analogRead(A0);

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  sendDataToServer(temperature, humidity, lightLevel);
  delay(10000); // Wait 10 seconds before sending data again
}

void connectToWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi!");
}

void sendDataToServer(float temperature, float humidity, int lightLevel) {
  if (client.connect(SERVER, 80)) {
    client.print("POST /upload_data HTTP/1.1\r\n");
    client.print("Host: ");
    client.print(SERVER);
    client.print("\r\n");
    client.print("Content-Type: application/x-www-form-urlencoded\r\n");
    client.print("Connection: close\r\n");
    client.print("\r\n");
    client.print("temperature=");
    client.print(temperature);
    client.print("&humidity=");
    client.print(humidity);
    client.print("&lightLevel=");
    client.print(lightLevel);
    client.print("\r\n");
  }
}
