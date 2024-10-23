from turtle import Turtle

LINE_DASH_SEPARATION = 20

class MiddleLine:

    def __init__(self, canvas_height):
        self.canvas_height = canvas_height
        self.md = Turtle()
        self.md.speed("fastest")
        self.position()
        self.draw()


    def position(self):
        self.md.hideturtle()
        self.md.color("white")
        self.md.width(5)
        self.md.penup()
        self.md.goto(x=0, y=-self.canvas_height / 2)
        self.md.setheading(90)

    def draw(self):
        # Number of line and separation in the dashed line
        n_dashes = (self.canvas_height // (2 * LINE_DASH_SEPARATION)) + 1
        for dash in range(n_dashes):
            self.md.pendown()
            self.md.fd(LINE_DASH_SEPARATION)
            self.md.penup()
            self.md.fd(LINE_DASH_SEPARATION)