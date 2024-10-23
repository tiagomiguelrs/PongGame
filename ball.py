from turtle import Turtle
from random import randint

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
BALL_SPEED = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.set_start_direction()
        self.velocity = 0.05

    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.penup()

    def refresh(self):
        self.velocity = 0.05
        self.goto(0, 0)
        self.set_start_direction()

    def set_start_direction(self):
        angle = 90
        side = randint(0, 1)
        if side == 0:
            angle += randint(45, 135)
        elif side == 1:
            angle += randint(225, 315)
        full_rotations = angle % 360
        self.setheading(angle - full_rotations * 360)

    def move_ball(self):
        self.fd(BALL_SPEED)

    def bounce_off_wall(self):
        new_angle = 0

        if self.ycor() > 0:
            if 0 <= self.heading() < 90:
                normal_angle = 0
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() - reflect + 360
            elif 90 <= self.heading() < 180:
                normal_angle = 180
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() + reflect

        if self.ycor() < 0:
            if 180 <= self.heading() < 270:
                normal_angle = 180
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() - reflect
            elif 270 <= self.heading() < 360:
                normal_angle = 360
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() + reflect - 360

        self.setheading(new_angle)

    def bounce_off_paddle(self):
        new_angle = 0
        random_angle = randint(-40, 40)
        if self.xcor() > 0:
            if 0 <= self.heading() < 90:
                normal_angle = 90
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() + reflect
            elif 270 <= self.heading() < 360:
                normal_angle = 270
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() - reflect

        if self.xcor() < 0:
            if 90 <= self.heading() < 180:
                normal_angle = 90
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() - reflect
            elif 180 <= self.heading() < 270:
                normal_angle = 270
                reflect = 2 * abs(normal_angle - self.heading())
                new_angle = self.heading() + reflect

        self.setheading(new_angle + random_angle)
        self.velocity *= 0.9