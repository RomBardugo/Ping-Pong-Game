from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

playing = True

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while True:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reverse_dir()

    if ball.xcor() > 410:
        scoreBoard.increse_l_score()
        print("l point")
        ball.reset_position()
        # playing = False

    if ball.xcor() < -410:
        scoreBoard.increse_r_score()
        ball.reset_position()
        # playing = False

screen.exitonclick()
