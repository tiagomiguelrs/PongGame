from turtle import Turtle

PADDLE_WIDTH = 0.5
PADDLE_HEIGHT = 5

class Paddle(Turtle):

    def __init__(self, canvas_width, canvas_height, side):
        super().__init__()
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        if side == "left":
            self.side = -1
        elif side == "right":
            self.side = 1
        self.build_paddle()

    def build_paddle(self):
        self.format()
        self.position()

    def format(self):
        self.speed("fastest")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.color("white")

    def position(self):
        xpos = self.side * (self.canvas_width / 2 - 20)
        ypos = 0
        self.goto(xpos, ypos)

    def move_up(self):
        if self.ycor() < self.canvas_height/2:
            self.fd(20)

    def move_down(self):
        if self.ycor() > -self.canvas_height/2:
            self.bk(20)
