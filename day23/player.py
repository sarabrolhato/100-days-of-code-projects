# Defines the user class for the Turtle Crossing Game

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("OliveDrab")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def squish(self):
        self.shape("circle")
        self.color("red")

    def reset_position(self):
        self.goto(STARTING_POSITION)