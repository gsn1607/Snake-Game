from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.score_update()

    def score_update(self):
        self.write(arg=f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()
