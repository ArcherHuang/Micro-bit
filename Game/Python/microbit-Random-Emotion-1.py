# Add your Python code here. E.g.
from microbit import *
import random

while True:
    no = random.randint(0, 4)
    if no == 0:
        display.show(Image.HOUSE)
    elif no == 1:
        display.show(Image.DUCK)
    elif no == 2:
        display.show(Image.HAPPY)
    elif no == 3:
        display.show(Image.GHOST)
    elif no == 4:
        display.show(Image.HEART)
    sleep(1000)
