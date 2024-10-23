from turtle import Turtle

SCORE_DISPLAY = 50
CANVAS_HEIGHT = 600

class Scoreboard(Turtle):

    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.side = side
        if side == "right":
            self.goto(SCORE_DISPLAY, CANVAS_HEIGHT/2 - 50)
        elif side == "left":
            self.goto(-SCORE_DISPLAY, CANVAS_HEIGHT/2 - 50)
        self.board_update()

    def board_update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.board_update()

    def game_over(self):
        self.goto(0, 20)
        self.write(f"{self.side} wins!", align="center", font=("Arial", 30, "normal"))
