from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
screen = Screen()
screen.setup(width=1000, height=500)

bet = screen.textinput("Make your bet.", "Which color turtle will win the race?:")

fin_tur = Turtle("turtle")
fin_tur.hideturtle()
fin_tur.penup()
fin_tur.goto(x=450, y=250)
fin_tur.right(90)
fin_tur.pendown()
fin_tur.forward(520)
turtles = []
y = -120
is_race_on = False

for color in colors:
    new_tur = Turtle(shape="turtle")
    new_tur.penup()
    new_tur.color(color)
    new_tur.goto(-450, y)
    y += 40
    turtles.append(new_tur)

if bet:
    is_race_on = True

while is_race_on:
    for tur in turtles:
        tur.forward(random.randint(0, 10))
        if tur.xcor() >= 435:
            print(tur.pencolor(), "turtle Have won the race")
            is_race_on = False

if bet == tur:
    print("Congrats, You won the bet!!.")
else:
    print("Your Turtle lost the bet, Better luck next time!")

screen.exitonclick()
