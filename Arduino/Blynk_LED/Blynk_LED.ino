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
char auth[] = "a17a842931d740e4b01ac11fddb81d88";

// Create ble serial instance, parameters are ignored for MicroBit
BLESerial SerialBLE(0, 0, 0);

// Configure Pin
#define PIN_BUTTON_A 5
#define LED_ROW2 27
#define LED_COL3 10

BLYNK_WRITE(V0)
{
  pinMode(LED_ROW2, OUTPUT);
  pinMode(LED_COL3, OUTPUT);
  if (param.asInt() == 1)        /* When button widget is "ON" */
  {
    digitalWrite(LED_ROW2, 1);
    digitalWrite(LED_COL3, 0);
  }
  else
  {
    digitalWrite(LED_ROW2, 0);
    digitalWrite(LED_COL3, 0);
  }
}

void setup() 
{
  Serial.begin(9600);

  SerialBLE.setLocalName("Blynk");
  SerialBLE.setDeviceName("Blynk");
  SerialBLE.setAppearance(0x0080);
  SerialBLE.begin();

  Blynk.begin(SerialBLE, auth);

  Serial.println("Waiting for connections...");

  pinMode(PIN_BUTTON_A, INPUT_PULLUP);
}

void loop() 
{
  SerialBLE.poll();
  Serial.print("Button A Status: ");
  Serial.println(digitalRead(PIN_BUTTON_A));
  if (SerialBLE) {    // If BLE is connected...
    Blynk.run();
  }
}

