# **************************************************************************************************************************
# Version:     2017.8.5 
# Author:      Archer Huang
# License:     MIT
# Description: Send data to MCS
# **************************************************************************************************************************
# 
# 1. install Serial SDK
# 	 
#    pip install pyserial

import serial
import time
import httplib, urllib
import json

ser = serial.Serial('/dev/cu.usbmodem1422', 115200)
print(ser.name)

deviceId = "DiqArAAc"
deviceKey = "UaC0Z8G4YtwaADfU"

def post_to_mcs(payload):
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    temperature = ser.readline().strip()
    print(temperature)
    payload = {"datapoints":[{"dataChnId":"Temperature","values":{"value":temperature}}]}
    post_to_mcs(payload)
    time.sleep(10)

