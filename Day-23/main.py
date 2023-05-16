import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "w")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect successful crossing
    if player.ycor() > 280:
        player.refresh()
        scoreboard.increase_level()
        car_manager.increase_speed()

    screen.update()
    # Detect collision with car
    if car_manager.check_collision(player):
        screen.update()
        scoreboard.game_over()
        game_is_on = False
        car_manager.clear()

screen.exitonclick()
