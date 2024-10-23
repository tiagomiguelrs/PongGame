from turtle import Turtle, Screen
from middle_line import MiddleLine
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
PADDLE_WIDTH = 20
NUMBER_OF_TURTLES_IN_PADDLE = 3
GAME_ON = True

# Set the screen
screen = Screen()
screen.tracer(0)
screen.screensize(canvwidth=CANVAS_WIDTH, canvheight=CANVAS_HEIGHT, bg="black")

# Create a class that draws the middle
MiddleLine(canvas_height=CANVAS_HEIGHT)

# Create and move a paddle
paddle_right = Paddle(CANVAS_WIDTH, CANVAS_HEIGHT, side="right")
paddle_left = Paddle(CANVAS_WIDTH, CANVAS_HEIGHT, side="left")

# Create scoreboard
score_left = Scoreboard("left")
score_right = Scoreboard("right")

# Create a ball
ball = Ball()

screen.listen()
screen.onkeypress(fun=paddle_right.move_up, key="Up")
screen.onkeypress(fun=paddle_right.move_down, key="Down")
screen.onkeypress(fun=paddle_left.move_up, key="w")
screen.onkeypress(fun=paddle_left.move_down, key="s")

while GAME_ON:
    screen.update()

    # Make the ball move
    ball.move_ball()

    # print(ball.pos())
    # print()

    # Set ball collisions with wall
    if ball.xcor() < -CANVAS_WIDTH/2 or ball.xcor() > CANVAS_WIDTH/2 or ball.ycor() < -CANVAS_HEIGHT/2 or ball.ycor() > CANVAS_HEIGHT/2:
        ball.bounce_off_wall()

    # Detect ball collision with paddle
    y_pos, x_pos = ball.pos()
    if paddle_right.distance((y_pos, x_pos)) < 50 and ball.xcor() > paddle_right.xcor()-10:
        ball.bounce_off_paddle()

    if paddle_left.distance((y_pos, x_pos)) < 50 and ball.xcor() < paddle_left.xcor()+10:
        ball.bounce_off_paddle()

    # Detect goals
    if ball.xcor() > paddle_right.xcor()+10:
        score_left.increase_score()
        ball.refresh()
        if score_left.score > 3:
            score_left.game_over()
            GAME_ON = False

    if ball.xcor() < paddle_left.xcor()-10:
        score_right.increase_score()
        ball.refresh()
        if score_right.score > 3:
            score_right.game_over()
            GAME_ON = False

    sleep(ball.velocity)

screen.mainloop()