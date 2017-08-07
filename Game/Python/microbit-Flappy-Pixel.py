from microbit import *
import random

pixel_row = 2
gate_column = 4
gate_row = 1
gate_size = 3
gate_move = False
score = 0

while True:
    y = accelerometer.get_y()
    if y > 600 and pixel_row < 4:
        pixel_row += 1
    elif y <= 600 and pixel_row > 0:
        pixel_row -= 1
    if gate_move:
        gate_column -= 1
    gate_move = not gate_move
    display.clear()
    display.set_pixel(0, pixel_row, 8)
    for i in range(5):
        if i < gate_row or i > gate_row + gate_size - 1:
            display.set_pixel(gate_column, i, 5)
    if gate_column == 0:
        if pixel_row < gate_row or pixel_row > gate_row + gate_size - 1:
            break
        score += 1
        if score in (1, 10):
            gate_size -= 1
        gate_column = 4
        gate_row = random.randint(0, 4 - gate_size + 1)
    sleep(400)
sleep(800)
display.scroll("You scored " + str(score) + " points!")