# Add your Python code here. E.g.
from microbit import *
import random

catchCount = 3
totalCount = 0
list1 = []
while True:
    if button_a.is_pressed():
        display.clear()
        list1 = [1,2,3,4,5,6]
    if button_b.is_pressed():  
        for x in range(catchCount):
            arrayLength = len(list1)
            randomNo = random.randint(0, arrayLength - 1)
            #display.show(str(randomNo))
            display.show(str(list1.pop(randomNo)))
            sleep(1000)
