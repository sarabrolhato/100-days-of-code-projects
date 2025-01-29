import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

NUMBER_OF_CARS = 30

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0) # Turns animation tracer off, so that the screen will only update when we tell it to

tortoise = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Controling the turtle with a keypress
screen.listen()
screen.onkeypress(tortoise.go_up, "Up")

game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
    #     # if (tortoise.xcor() == car.xcor() - 35) and ((tortoise.ycor() < car.ycor() + 10) and (tortoise.ycor() > car.ycor() - 10)):
        if ((tortoise.xcor() < car.xcor() + 30) and (tortoise.xcor() > car.xcor() - 30)) and ((tortoise.ycor() < car.ycor() + 20) and tortoise.ycor() > car.ycor() - 20):
            tortoise.squish()
            screen.update()
            scoreboard.game_over()
            game_is_on = False
                                                
    # Detect successful crossing
    if tortoise.ycor() > 250:
        scoreboard.level_up()
        tortoise.reset_position()
        car_manager.increase_speed()


screen.exitonclick()