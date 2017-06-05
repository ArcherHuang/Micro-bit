/*************************************************************
 * 
  This example shows how to use BBC Micro:Bit
  to connect your project to Blynk.
  Note: This requires nRF5 support package:
    https://github.com/sandeepmistry/arduino-nRF5
  And BLEPeripheral library
    from http://librarymanager/all#BLEPeripheral
    or https://github.com/sandeepmistry/arduino-BLEPeripheral
  1. Select: Tools -> SoftDevice -> S110
  2. Select: Tools -> Programmer -> CMSIS-DAP
  3. Select: Tools -> nRF5 Flash SoftDevice
  4. Read and Accept License
  5. Verify and Upload Sketch
  NOTE: BLE support is in beta!
 *************************************************************/

#define BLYNK_USE_DIRECT_CONNECT

#define BLYNK_PRINT Serial

#include <BlynkSimpleSerialBLE.h>
#include <BLEPeripheral.h>
#include "BLESerial.h"

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "cde201ebef43491da1cf683bbfdcee54";

// Create ble serial instance, parameters are ignored for MicroBit
BLESerial SerialBLE(0, 0, 0);

// Configure Pin
#define LightPin 0

void setup() 
{
  Serial.begin(9600);

  SerialBLE.setLocalName("Blynk");
  SerialBLE.setDeviceName("Blynk");
  SerialBLE.setAppearance(0x0080);
  SerialBLE.begin();

  Blynk.begin(SerialBLE, auth);

  Serial.println("Waiting for connections...");

}

void loop() 
{
  float lightSensingData = analogRead(LightPin);
  Serial.print("Light Sensor: "); 
  Serial.println(lightSensingData);
  if (SerialBLE) {    // If BLE is connected...
    Blynk.run();
    Blynk.virtualWrite(V0, lightSensingData);
  }
  delay(1000); //每秒回傳一次資料
}
