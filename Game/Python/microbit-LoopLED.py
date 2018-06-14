# Add your Python code here. E.g.
from microbit import *

while True:
    if button_a.is_pressed():
        display.clear()
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,9)
                sleep(100)
