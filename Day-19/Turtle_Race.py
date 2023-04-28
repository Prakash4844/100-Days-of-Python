from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
screen = Screen()
screen.setup(width=1000, height=500)

bet = screen.textinput("Make your bet.", "Which color turtle will win the race?:")
tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.goto(x=-450, y=-200)

print(bet)






screen.exitonclick()
