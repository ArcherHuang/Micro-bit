# Add your Python code here. E.g.
from microbit import *

while True:
    if button_a.is_pressed():
        no = 9
        for x in range(10):
            display.show(str(no))
            sleep(1000)
            no = no -1
