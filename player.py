# IMPORT LIST #
from turtle import Turtle

# CONSTANT #
starting_position = (0,-250)
move_distance = 15


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.start_position()


    def start_position(self):
        self.goto(starting_position)

    def move_right(self):
        self.forward(move_distance)

    def move_left(self):
        self.back(move_distance)

