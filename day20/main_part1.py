# Snake Game - Part 1

# This file sets up the screen, creates the snake's body and animates the snake's segments on the screen.

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0) # Turns animation tracer off, so that the screen will only update when we tell it to using the update method

segments = []

# Create the snake
for i in range(0, 3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    x_pos = i * (-20)
    new_segment.penup()
    new_segment.goto(x=x_pos, y=0)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update() # Performs a screen update
    time.sleep(0.1) # Adds a delay
    
    # Move the snake
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) 
    segments[0].forward(20)


screen.exitonclick()