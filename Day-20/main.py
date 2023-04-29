from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jehrilla")
screen.tracer(0)

game_on = True
snake = Snake()

screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='d', fun=snake.right)

screen.update()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
