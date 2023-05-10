from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Noto Sans", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 180)
        self.write(f"{self.l_score}", align="center", font=FONT)
        self.goto(150, 180)
        self.write(f"{self.r_score}", align="center", font=FONT)

    def game_over(self, alignment):
        # self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER!, {alignment.title()} Player has won!", align="center", font=FONT)
