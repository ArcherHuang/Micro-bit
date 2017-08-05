# **************************************************************************************************************************
# Version:     2017.8.5 
# Author:      Archer Huang
# License:     MIT
# Description: Send data to ThingSpeak
# **************************************************************************************************************************
# 
# 1. ThingSpeak
#    https://thingspeak.com/
#
# 2. install Serial SDK
#    pip install pyserial

import serial
import time
import httplib, urllib
import json

ser = serial.Serial('/dev/cu.usbmodem1422', 115200)
print(ser.name)

apiKey = "F674M0GR2WOTYQD5"

def post_to_thingspeak(payload):
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.thingspeak.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/update", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    sensingData = ser.readline().strip()
    print(sensingData)
    sensingDataArray = sensingData.split(':')
    print(sensingDataArray)
    params = urllib.urlencode({'field1': sensingDataArray[0], 'field2': sensingDataArray[1], 'key': apiKey})
    post_to_thingspeak(params)
    time.sleep(10)

