import random
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("medium slate blue")
t.colormode(255)

########### Challenge 4 - Draw a Random Walk ########
#
# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue",
#           "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black"]


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    rgb = (r, g, b)
    return rgb


angeles = [0, 90, 180, 270]
tim.width(10)
tim.speed("fastest")

for _ in range(200):
    tim.forward(20)
    tim.setheading(random.choice(angeles))
    tim.color(random_color())


tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
