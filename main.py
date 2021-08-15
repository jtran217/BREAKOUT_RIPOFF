# IMPORTS #
from turtle import Screen
from player import Player
from ball import Ball
from wall import WallManager
from scoreboard import ScoreBoard
import time



# GAME LOGIC #
screen = Screen()
screen.title("BREAKOUT")
screen.setup(width=600,height=800)
screen.tracer(0)
screen.bgcolor('black')


player = Player()
ball = Ball()
screen.update()
wallmanager = WallManager()
scoreboard = ScoreBoard()

screen.update()
screen.listen()
screen.onkey(player.move_right,'Right')
screen.onkey(player.move_left,'Left')

game_mode = True
while game_mode:
    time.sleep(0.1)
    screen.update()
    wallmanager.create_wall()
    screen.update()
    ball.move()

    # IF BALL PASS SCREEN LIMIT X IT SHOULD BOUNCE
    if ball.xcor() > 298 or ball.xcor() < -298:
        ball.bounce_x()

    # IF BALL HITS PADDLE IT SHOULD BOUNCE
    if ball.distance(player) < 30 and ball.ycor() > -250:
        ball.bounce_y()

    # IF BALL HITS ONE OF THE WALLS IT SHOULD TURN INVISIBLE AND SCORE PLAYER WITH POINT
    if ball.ycor() > 5:
        for object in wallmanager.all_wall:
            if ball.distance(object) < 30 and object.isvisible():
                object.hideturtle()
                scoreboard.score_point()
                ball.bounce_y()
            else:
                pass
    # IF BALL HITS TOP
    if ball.ycor() > 398:
        ball.bounce_y()
    # LOSE CONDITION
    if ball.ycor() < -400:
        scoreboard.lose_update()
        game_mode = False

    # INCREASE SPEED OF BALL BASED ON CURRENT SCORE
    if scoreboard.score > 1:
        if scoreboard.score / 4 == 0:
            ball.increase_difficulty()

screen.exitonclick()