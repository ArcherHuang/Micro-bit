from microbit import *
from random import randrange


class Snake():
    def __init__(self):
        self.length = 2
        self.direction = "down"
        self.head = (2, 2)
        self.tail = []

    def move(self):
        # extend tail
        self.tail.append(self.head)

        # check snake size
        if len(self.tail) > self.length - 1:
            self.tail = self.tail[-(self.length - 1):]

        if self.direction == "left":
            self.head = ((self.head[0] - 1) % 5, self.head[1])
        elif self.direction == "right":
            self.head = ((self.head[0] + 1) % 5, self.head[1])
        elif self.direction == "up":
            self.head = (self.head[0], (self.head[1] - 1) % 5)
        elif self.direction == "down":
            self.head = (self.head[0], (self.head[1] + 1) % 5)

    def grow(self):
        self.length += 1

    def collides_with(self, position):
        return position == self.head or position in self.tail

    def draw(self):
        # draw head
        display.set_pixel(self.head[0], self.head[1], 9)

        # draw tail
        brightness = 8
        for dot in reversed(self.tail):
            display.set_pixel(dot[0], dot[1], brightness)
            brightness = max(brightness - 1, 5)


class Fruit():
    def __init__(self):
        # place in a random position on the screen
        self.position = (randrange(0, 5), randrange(0, 5))

    def draw(self):
        display.set_pixel(self.position[0], self.position[1], 9)


class Game():
    def __init__(self):
        self.player = Snake()
        self.place_fruit()

    def place_fruit(self):
        while True:
            self.fruit = Fruit()
            # check it's in a free space on the screen
            if not self.player.collides_with(self.fruit.position):
                break

    def handle_input(self):
        # change direction? (no reversing)
        if button_a.is_pressed() and button_b.is_pressed():
            if self.player.direction != "down":
                self.player.direction = "up"
        elif button_a.is_pressed():
            if self.player.direction != "right":
                self.player.direction = "left"
        elif button_b.is_pressed():
            if self.player.direction != "left":
                self.player.direction = "right"
        else:
            if self.player.direction != "up":
                self.player.direction = "down"

    def update(self):
        # move snake
        self.player.move()

        # game over?
        if self.player.head in self.player.tail:
            self.game_over()

        # nom nom nom
        elif self.player.head == self.fruit.position:
            self.player.grow()

            # space for more fruit?
            if self.player.length < 5 * 5:
                self.place_fruit()
            else:
                self.game_over()

    def score(self):
        return self.player.length - 2

    def game_over(self):
        display.scroll("Score: %s" % self.score())
        reset()

    def draw(self):
        display.clear()
        self.player.draw()
        self.fruit.draw()


game = Game()

# main game loop
while True:
    game.handle_input()
    game.update()
    game.draw()
    sleep(500)