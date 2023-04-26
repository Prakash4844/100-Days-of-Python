import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("medium slate blue")

######## Challenge 2 - Draw Dashed line ############
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen = t.Screen()
screen.exitonclick()