#include <SoftwareSerial.h>
#include <DHT.h>

#define DHT_SENSOR_PIN 7            // Pin connected to the DHT sensor
#define DHT_SENSOR_TYPE DHT22       // Type of DHT sensor used

#define WIFI_SSID "Wokwi-GUEST"     // WiFi network name (SSID)
#define WIFI_PASSWORD ""            // WiFi password (if any)

#define SERVER_ADDRESS "iot-temperature-monitoring-mock-server.free.beeceptor.com" // Server to send data to
#define SERVER_URL "https://app.beeceptor.com/console/iot-temperature-monitoring-mock-server" // Console URL

DHT dht(DHT_SENSOR_PIN, DHT_SENSOR_TYPE);  // Set up DHT sensor
SoftwareSerial esp8266(2, 3);              // RX (2) and TX (3) pins for ESP8266 communication

// Helper function for logging messages with a description
void logStatus(const String& stage, const String& info) {
  Serial.print(stage + ": ");
  Serial.println(info);
}

// Function to initialize the ESP8266 module
void initializeESP8266() {
  logStatus("Starting Initialization", "ESP8266 module");

  // Reset ESP8266
  sendATCommand("AT+RST\r\n", 2000, "Resetting ESP8266 module");
  
  // Set ESP8266 to WiFi Station mode
  sendATCommand("AT+CWMODE=1\r\n", 1000, "Setting WiFi mode to Station");
  
  // Connect to the WiFi network
  sendATCommand("AT+CWJAP=\"" + String(WIFI_SSID) + "\",\"" + String(WIFI_PASSWORD) + "\"\r\n", 5000, "Connecting to WiFi");

  // Request the IP address of the ESP8266
  sendATCommand("AT+CIFSR\r\n", 1000, "Getting ESP8266 IP address");

  logStatus("Initialization Complete", "ESP8266 ready");

  logStatus("\nConsole URL", SERVER_URL);
}

// Function to send temperature data to the server via HTTP POST request
void transmitTemperature(float temp) {
  // Convert the temperature to a string with two decimal places
  String tempStr = String(temp, 2);
  
  // Formulate the HTTP POST request
  String httpRequest = "POST / HTTP/1.1\r\n";
  httpRequest += "Host: " + String(SERVER_ADDRESS) + "\r\n";
  httpRequest += "Content-Type: application/x-www-form-urlencoded\r\n";
  httpRequest += "Content-Length: " + String(tempStr.length()) + "\r\n";
  httpRequest += "Connection: close\r\n\r\n";
  httpRequest += tempStr;

  logStatus("HTTP Request", "Sending temperature data...");

  // Open a TCP connection to the server
  sendATCommand("AT+CIPSTART=\"TCP\",\"" + String(SERVER_ADDRESS) + "\",80\r\n", 5000, "Connecting to server");

  // Inform the ESP8266 of the size of the request data
  sendATCommand("AT+CIPSEND=" + String(httpRequest.length()) + "\r\n", 2000, "Sending request size");

  // Send the actual HTTP request body
  sendATCommand(httpRequest, 2000, "Transmitting data to server");
}

// Function to send an AT command and check for a response
void sendATCommand(String command, int timeout, const String& description) {
  String response = "";
  esp8266.print(command);
  
  long int startMillis = millis();
  while ((startMillis + timeout) > millis()) {
    while (esp8266.available()) {
      char receivedChar = (char)esp8266.read();
      if (isPrintable(receivedChar) || receivedChar == '\n' || receivedChar == '\r') {
        response += receivedChar;
      }
    }
  }

  // Check the response for success or failure
  if (response.indexOf("OK") >= 0) {
    logStatus("Response", "Success");
  } else if (response.indexOf("ERROR") >= 0) {
    logStatus("Response", "Error: " + response);
  } else {
    logStatus("Response", "Unexpected Response");
  }
}

void setup() {
  Serial.begin(115200);  // Start serial communication at 115200 baud
  esp8266.begin(115200);  // Initialize SoftwareSerial for ESP8266 communication
  dht.begin();            // Initialize the DHT sensor
  initializeESP8266();    // Initialize ESP8266 WiFi module
}

void loop() {
  delay(2000);  // Delay between temperature readings

  // Read the temperature from the DHT sensor
  float temperature = dht.readTemperature();
  if (isnan(temperature)) {
    logStatus("Error", "Failed to read temperature from DHT sensor.");
    return;
  }
  
  // Log the temperature to the Serial Monitor
  logStatus("Temperature", String(temperature, 2) + "°C");
  
  // Send the temperature data to the server
  transmitTemperature(temperature);
}
