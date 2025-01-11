# The Turtle Racing Game

from turtle import Turtle, Screen
import random

# Creating a variable to let the race start at the right moment
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

# Ask for user's bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Setting initial y axis
y= -100
# Placing turtles to their initial position
for i in range(1,7):
   new_turtle = Turtle(shape="turtle")
   new_turtle.color(colors[i-1])
   new_turtle.penup()
   new_turtle.goto(x=-220, y=y)
   y += 40
   all_turtles.append(new_turtle)

# The race starts when all turtles are in their position
if user_bet:
   is_race_on = True

while is_race_on:
   for turtle in all_turtles:
      # In each round, checks if any turtle has reached the finish line
      if turtle.xcor() > 230: # 230 because a turtle has length of 20
         is_race_on = False
         winning_color = turtle.pencolor()
         if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
         else:
            print(f"You've lost! The {winning_color} turtle is the winner!")
         
      # In each round, turtles move a random distance
      rand_distance = random.randint(0, 10)
      turtle.forward(rand_distance)


screen.exitonclick()