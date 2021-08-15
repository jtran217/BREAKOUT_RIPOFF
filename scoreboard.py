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
        self.write(f'Score: {self.score}',align='center', font=("Courier", 60, "normal"))

    def score_point(self):
        self.score += 1
        self.update_score()

    def lose_update(self):
        self.clear()
        self.goto(0,300)
        self.write(f"GAME OVER,SCORE: {self.score}",align='center', font=("Courier", 40, "normal"))
