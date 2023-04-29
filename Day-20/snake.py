from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]

    def create_snake(self):
        for i in range(3):
            new_snake_part = Turtle("square")
            new_snake_part.penup()
            new_snake_part.color("white")
            new_snake_part.goto(-20 * i, 0)
            self.snake_seg.append(new_snake_part)

    def move(self):
        for sn in range(len(self.snake_seg) - 1, 0, -1):
            new_x = self.snake_seg[sn - 1].xcor()
            new_y = self.snake_seg[sn - 1].ycor()
            self.snake_seg[sn].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
