# The Hirst Painting Project

from turtle import Turtle, Screen
import random
import colorgram

turtle = Turtle()
turtle.shape("turtle")
turtle.width(20)
turtle.speed(0)
turtle.penup()
turtle.hideturtle()
screen = Screen()
screen.colormode(255)


# Extracting 10 colors from the Damien Hirst painting
colors = colorgram.extract("day18\\DamienHirst.jpg", 20)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# We create a new list after removing the white shades
color_list = [(249, 240, 246), (109, 173, 204), (203, 168, 11), (33, 121, 154), (233, 144, 74), (204, 134, 175), (175, 10, 71), (206, 79, 116), (230, 207, 116), (156, 60, 116), (160, 96, 26), (231, 165, 189), (119, 194, 174), (50, 171, 108), (25, 148, 91), (76, 17, 10), (34, 156, 193)]

# Setting the turtle's initial position
turtle.teleport(-200,-200)

for i in range (1, 11):

    for j in range(9):
        turtle.dot(20, random.choice(color_list))
        
        turtle.forward(50)

    turtle.dot(20, random.choice(color_list))

    if i % 2 == 0:
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    else:
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    

screen.exitonclick()
