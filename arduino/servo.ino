#include <ESP8266WiFi.h>
#include <Servo.h>

const char* ssid = YOUR_WIFI_NAME;
const char* password = YOUR_WIFI_PASSWORD;
const int servoPin = 2; 

Servo servo;
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  Serial.println("Connecting to Wi-Fi...");

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("NodeMCU(ESP8266) is connected to the Wi-Fi");
    Serial.println("IP Address: " + WiFi.localIP().toString());
  } else {
    Serial.println("Failed to connect to Wi-Fi");
  }

  pinMode(servoPin, OUTPUT);
  servo.attach(servoPin);

  server.begin();
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    Serial.println("Client connected");
    
    String request = client.readStringUntil('\n');
    client.flush();
    Serial.println(request);

    if (request.indexOf("rotate?direction=left") != -1) {
      rotateServoLeft();
      Serial.println("Servo rotating left");
    } else if (request.indexOf("rotate?direction=right") != -1) {
      rotateServoRight();
      Serial.println("Servo rotating right");
    }

    client.println("HTTP/1.1 200 OK");
    Serial.println("Client Disconnected");
    Serial.println("===========================================================");
    Serial.println("                              ");
  }
}

void rotateServoLeft() {
  servo.write(10);  // Change the angle for your specific servo
  delay(1000);
  servo.write(90);  
}

void rotateServoRight() {
  servo.write(170);  // Change the angle for your specific servo
  delay(1000);
  servo.write(90);   
}
