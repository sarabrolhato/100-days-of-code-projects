from turtle import Turtle
import random

# List of possible car colors
# colors = ["MediumTurquoise", "PaleVioletRed", "SteelBlue", "salmon", "DarkSeaGreen1", "hotpink", "DarkOrange"]

colors = [
    "MediumTurquoise", 
    "PaleVioletRed", 
    "SteelBlue", 
    "salmon", 
    "lightcoral", 
    "lavender", 
    "lightblue", 
    "lightgreen", 
    "lightpink", 
    "lightskyblue", 
    "lightgrey", 
    "lightcyan", 
    "plum", 
    "orchid", 
    "thistle" 
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.setheading(180)
            y_pos = random.uniform(-250, 250)
            new_car.goto(300, y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT