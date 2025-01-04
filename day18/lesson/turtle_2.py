from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("RoyalBlue4")
turtle.width(5)
turtle.speed(0)

screen = Screen()

# Drawing a dashed line

for _ in range(10):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen.exitonclick()