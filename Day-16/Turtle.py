from turtle import Turtle, Screen
import prettytable

rex = Turtle()
rex.shape("turtle")
rex.color("red")
screen = Screen()
rex.forward(100)
print(screen.canvwidth)
screen.exitonclick()
