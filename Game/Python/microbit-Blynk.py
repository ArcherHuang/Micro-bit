# Add your Python code here. E.g.
from microbit import *

while True:
    ledOn = Image("00000:"
                "00000:"
                "00100:"
                "00000:"
                "00000")
    ledOff = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
    all_led = [ledOn, ledOff]
    display.show(all_led, delay=1000)
