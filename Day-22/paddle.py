from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() <= 160:
            print(f"x = {self.xcor()}, y = {self.ycor()}")
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -164:
            print(f"x = {self.xcor()}, y = {self.ycor()}")
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

