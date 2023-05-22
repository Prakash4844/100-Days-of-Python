from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Noto Sans", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Hi-Score.txt") as data:
            self.hiscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=280)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=280)
        self.write(f"High Score = {self.hiscore}", align=ALIGNMENT, font=FONT)

    def save_hiscore(self):
        with open("Hi-Score.txt", mode="w") as data:
            data.write(str(self.hiscore))

    def reset_score(self):
        self.save_hiscore()
        self.score = 0
        self.update_score()

    def increase_score(self):
        if self.score >= self.hiscore:
            self.hiscore += 1
        self.score += 1
        self.update_score()

