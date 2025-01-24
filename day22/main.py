# Pong Game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turns animation tracer off, so that the screen will only update when we tell it to

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# Controling the snake with a keypress
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with upper and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right and left paddles
    if (
        (ball.xcor() == r_paddle.xcor() - 20) and ((ball.ycor() < r_paddle.ycor() + 60) and (ball.ycor() > r_paddle.ycor() - 60)) # Right paddle
        or
        (ball.xcor() == l_paddle.xcor() + 20) and ((ball.ycor() < l_paddle.ycor() + 60) and (ball.ycor() > l_paddle.ycor() - 60)) # Left paddle
    ):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
