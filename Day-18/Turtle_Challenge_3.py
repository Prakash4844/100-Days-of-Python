import random
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")

########### Challenge 3 - Draw Shapes ########
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue",
          "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black"]

for _ in range(3, 10):
    timmy_the_turtle.color(colors.pop(random.randint(0, len(colors)-1)))
    angle = 360/_
    while not _ == 0:
        timmy_the_turtle.left(angle)
        timmy_the_turtle.forward(100)
        _ -= 1

timmy_the_turtle.hideturtle()

screen = t.Screen()
screen.exitonclick()
