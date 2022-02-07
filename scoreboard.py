from turtle import Turtle
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230, 260)
        self.hideturtle()
        self.level = 1
        self.write(arg=f"level: {self.level}", font=FONT, align="center")

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"level: {self.level}", font=FONT, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", font=FONT, align="center")
