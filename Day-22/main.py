from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=868, height=460)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddle(position=(395, 0))
l_paddle = Paddle(position=(-395, 0))
# screen.tracer(1)
ball = Ball()
screen.update()

screen.listen()
screen.onkey(key='w', fun=r_paddle.up)
screen.onkey(key='s', fun=r_paddle.down)

screen.onkey(key='i', fun=l_paddle.up)
screen.onkey(key='k', fun=l_paddle.down)

game_on = True

while game_on:
    ball.move()
    time.sleep(0.07)
    screen.update()

screen.exitonclick()
