# The Snake Game - Part 2

# In this file, we will set up the screen, create and animate the snake's body using Object Oriented Programming
# We will create a snake class to include all snake-related functionalities.

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0) # Turns animation tracer off, so that the screen will only update when we tell it to

snake = Snake()

# Controling the snake with a keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()