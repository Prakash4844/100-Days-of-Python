from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jehrilla")
screen.tracer(0)

game_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

    # Detect collision with food
    if snake.head.distance(food) < 17:
        scoreboard.increase_score()
        food.refresh()
        snake.extend_snake()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() \
            < -280:
        game_on = False

    # Detect Collision with Tail
    for segments in snake.snake_seg[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            scoreboard.game_over()
scoreboard.game_over()


screen.exitonclick()
