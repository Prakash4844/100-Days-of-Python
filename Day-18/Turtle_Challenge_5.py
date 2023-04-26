import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(0, 360, size_of_gap):
        tim.setheading(_)
        tim.color(random_color())
        tim.circle(100)


enter = int(t.textinput(title="Spirograph", prompt="Enter the size of gap: "))

draw_spirograph(enter)

tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
