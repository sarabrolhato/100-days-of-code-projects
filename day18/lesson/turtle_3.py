from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("RoyalBlue4")
turtle.width(1.5)

screen = Screen()
screen.colormode(255)

# Drawing different shapes

for i in range(3, 11):

    angle = 360 / i

    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for j in range(i):
        turtle.forward(100)
        turtle.right(angle)


screen.exitonclick()