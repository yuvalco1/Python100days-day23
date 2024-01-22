from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto(x=-230, y=270)
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.score_write()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)