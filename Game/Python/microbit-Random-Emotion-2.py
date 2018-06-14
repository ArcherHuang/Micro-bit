# Add your Python code here. E.g.
from microbit import *
import random

while True:
    Img_list = [Image.HOUSE, Image.DUCK, Image.HAPPY, Image.GHOST, Image.HEART]
    image = random.choice(Img_list)
    display.show(image)
    sleep(1000)
