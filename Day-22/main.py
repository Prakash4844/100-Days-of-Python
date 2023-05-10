from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=868, height=460)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddle(position=(395, 0))
l_paddle = Paddle(position=(-395, 0))
screen.update()
screen.tracer(1)

screen.listen()
screen.onkey(key='w', fun=r_paddle.up)
screen.onkey(key='s', fun=r_paddle.down)

screen.onkey(key='i', fun=l_paddle.up)
screen.onkey(key='k', fun=l_paddle.down)

game_on = True

# while game_on:
#     screen.update()

screen.exitonclick()
