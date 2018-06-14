# Add your Python code here. E.g.
from microbit import *
import music

while True:
    if temperature() > 30:
        display.show(Image.NO)
        sleep(5000)
        display.clear()
        sleep(1000)
