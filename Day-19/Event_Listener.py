from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("medium slate blue")

screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="d", fun=move_forward)

screen.exitonclick()
