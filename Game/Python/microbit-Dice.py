# Add your Python code here. E.g.
from microbit import *
import random

display.show('-')

while True:
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.show(str(random.randint(1,6)))
    sleep(10)
