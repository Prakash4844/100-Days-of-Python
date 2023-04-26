##### Turtle Intro ######
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("medium slate blue")

######## Challenge 1 - Draw a Square ############
for _ in range(4):
    timmy_the_turtle.forward(200)
    timmy_the_turtle.right(90)


screen = t.Screen()
screen.exitonclick()
