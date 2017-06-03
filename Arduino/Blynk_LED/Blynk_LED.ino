/*************************************************************
  Blynk is a platform with iOS and Android apps to control
  Arduino, Raspberry Pi and the likes over the Internet.
  You can easily build graphic interfaces for all your
  projects by simply dragging and dropping widgets.

    Downloads, docs, tutorials: http://www.blynk.cc
    Sketch generator:           http://examples.blynk.cc
    Blynk community:            http://community.blynk.cc
    Social networks:            http://www.fb.com/blynkapp
                                http://twitter.com/blynk_app

  Blynk library is licensed under MIT license
  This example code is in public domain.

 *************************************************************

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

// Configure on-board buttons
//pinMode(PIN_BUTTON_A, INPUT_PULLUP);
//pinMode(PIN_BUTTON_B, INPUT_PULLUP);

#define LED_ROW2 27
#define LED_COL3 10
#define buttonPin 17

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

void setup() {
  Serial.begin(9600);

  SerialBLE.setLocalName("Blynk");
  SerialBLE.setDeviceName("Blynk");
  SerialBLE.setAppearance(0x0080);
  SerialBLE.begin();

  Blynk.begin(SerialBLE, auth);

  Serial.println("Waiting for connections...");

  pinMode(buttonPin, INPUT);
}

void loop() {
  SerialBLE.poll();
  Serial.print("Button Status: ");
  Serial.println(digitalRead(buttonPin));
  if (SerialBLE) {    // If BLE is connected...
    Blynk.run();
  }
}

