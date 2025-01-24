# Defining the Paddle class for the Pong Game

from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=None)
        self.color("white")
        self.speed("fastest")
        self.goto(paddle_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
