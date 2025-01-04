from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("RoyalBlue4")
turtle.width(15)
turtle.speed(10)

screen = Screen()
screen.colormode(255)

# Drawing a Random Walk

directions = [0, 90, 180, 270]

for i in range(150):
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.right(random.choice(directions))
    turtle.forward(30)


screen.exitonclick()