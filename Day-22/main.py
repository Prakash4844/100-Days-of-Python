from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=868, height=460)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddle(position=(395, 0))
l_paddle = Paddle(position=(-395, 0))
scoreboard = ScoreBoard()
# screen.tracer(1)
ball = Ball()
screen.update()

screen.listen()
screen.onkey(key='i', fun=r_paddle.up)
screen.onkey(key='k', fun=r_paddle.down)

screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)

game_on = True
sleep = 0.07

while game_on:
    ball.move()
    # print(f"x = {ball.xcor()}, y = {ball.ycor()}")
    time.sleep(sleep)
    screen.update()

    # Detect collision with wall
    if ball.ycor() >= 220 or ball.ycor() <= -220:
        ball.bounce_y()

    # print(ball.distance(r_paddle))
    # Detect collision with paddle
    if ball.distance(r_paddle) < 59 and ball.xcor() > 380 or ball.distance(l_paddle) < 59 and ball.xcor() < \
            -380:
        ball.bounce_x()
        sleep -= 0.005
        # print(sleep)

    # Detect when right paddle misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()
        sleep = 0.07
        # game_on = False

    # Detect when left paddle misses
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()
        sleep = 0.07
        # game_on = False

    # Detect when game is over
    if scoreboard.l_score == 10:
        scoreboard.game_over("left")
        game_on = False
    elif scoreboard.r_score == 10:
        scoreboard.game_over("right")
        game_on = False

screen.exitonclick()
