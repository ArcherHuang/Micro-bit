# **************************************************************************************************************************
# Version:     2017.8.5 
# Author:      Archer Huang
# License:     MIT
# Description: Get data from Serial Port 
# **************************************************************************************************************************
# 
# 1. install Serial SDK
# 	 
#    pip install pyserial

import serial
import time

ser = serial.Serial('/dev/cu.usbmodem1422', 115200)
print(ser.name)

while True:
	line = ser.readline()
	print(line) 
	time.sleep(1)
