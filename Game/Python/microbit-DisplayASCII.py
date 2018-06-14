# Add your Python code here. E.g.
from microbit import *

while True:
    for x in range(26):
        encrypted_char = chr(65 + x)
        display.show(encrypted_char)
        sleep(500)
