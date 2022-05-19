#include <ESP8266WiFi.h>
#include <ModbusIP_ESP8266.h>
#define APP_DEBUG
#define DHTTYPE DHT11
#include "DHT.h"

// Modbus Configurations
const int temperatureReg = 100;
const int brightStatusReg = 500;
IPAddress remote(192, 168, 1, 150);  // Address of Modbus Server
ModbusIP mb;

// Circuit Configurations
const int ldrPin = 5; // D1
const int dhtPin = 4; // D2
DHT dht;
  
void setup() {
  Serial.begin(115200);
  Serial.println("wifi connection started...");
  WiFi.begin("harman", "harman123");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
  
  pinMode(ldrPin, INPUT);
  dht.setup(dhtPin);
  
  mb.client();
}

uint16_t temperature = 1;
int brightStatus = -1;
 
void loop() {
  delay(3000);
  
  if (mb.isConnected(remote)) {
    Serial.println("connected");

    if(temperature != 65535){
      uint16_t transactionTemperature = mb.writeHreg(remote, temperatureReg, temperature, nullptr, MODBUSIP_UNIT);
      while(mb.isTransaction(transactionTemperature)) {  // Check if transaction is active
        mb.task();
        delay(10);
      }
    }

    if(brightStatus != 65535){
      uint16_t transactionBrightStatus = mb.writeHreg(remote, brightStatusReg, brightStatus, nullptr, MODBUSIP_UNIT);
      while(mb.isTransaction(transactionBrightStatus)){
        mb.task();
        delay(10);
      }
    }
  }else{
    Serial.println("Couldn't connected");
    mb.connect(remote, 8000);
  }
  
  temperature = dht.getTemperature();
  Serial.println(temperature);
  brightStatus = digitalRead(ldrPin);
  Serial.println(brightStatus);
}
