from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("RoyalBlue4")

screen = Screen()

# Draw a square

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)


screen.exitonclick()