# IMPORTS #
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0,300)
        self.write(f'Score: {self.score}',align='center', font=("Courier", 80, "normal"))

    def score_point(self):
        self.score += 1
        self.update_score()

    def lose_update(self):
        self.clear()
        self.goto(0,300)
        self.write("YOU LOSE",align='center', font=("Courier", 80, "normal"))
    def win_update(self):
        self.clear()
        self.goto(0,300)
        self.write("YOU WIN",align='center', font=("Courier", 80, "normal"))