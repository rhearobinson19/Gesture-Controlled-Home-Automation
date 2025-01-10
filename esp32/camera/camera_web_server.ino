#include <WiFi.h>
#include <esp_camera.h>

const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";

// WiFi initialization
void startCameraServer();

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  
  startCameraServer();
}

void loop() {
  delay(10000);
}
