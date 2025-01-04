from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("RoyalBlue4")
turtle.width(1)
turtle.speed(0)

screen = Screen()
screen.colormode(255)

# Drawing a circle

def draw_spirograph(n_circles):

    for i in range(1, n_circles + 1):

        angle = 360 / n_circles
        turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.circle(100)
        turtle.left(angle)
        turtle.circle(100)


draw_spirograph(n_circles=50)

screen.exitonclick()