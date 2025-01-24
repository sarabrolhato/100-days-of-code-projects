from turtle import Turtle

MOVE_DISTANCE = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.goto(0,0)
        self.delta_x = 2
        self.delta_y = 2
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.delta_y *= -1

    def bounce_x(self):
        self.delta_x *= -1
        # Increase ball speed
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        # Reset ball speed
        self.move_speed = 0.01

