# Higher Lower Game

# The goal of this project is to build a game that asks the user to guess who has more followers on Instagram.
# Original Higher Lower game: https://www.higherlowergame.com/

from art import logo
from art import vs
from game_data import data
import random
import os

# Defining a function that randomly selects an account
def select_account():
    return random.choice(data)

# Defining a function that prints the accounts to be compared
def print_comparison(item1, item2):
    print(f"Compare A: {item1["name"]}, a {item1["description"]}, from {item1["country"]}.")
    print(vs)
    print(f"Against B: {item2["name"]}, a {item2["description"]}, from {item2["country"]}.")

# Defining a function that checks answer
def check_answer(item1, item2):
    """Takes the two items to be compared, where the first item is the user's answer, and returns if the game is over (wrong answer) or not (they got it right)."""
    if item1["follower_count"] >= item2["follower_count"]:
        return False
    else:
        return True
    
# Print game logo
print(logo)

# Setting initial score to zero and creating game_over variable
score = 0
game_over = False

# Randomly selects the initial item A - just once
item_a = select_account()

# While person is correct, the game will continue
while game_over == False:
    # Randomly selects item B for this round
    item_b = select_account()
    # If item A and item B are the same, select item B again until they are different
    while item_a == item_b:
        item_b = select_account()

    # Prints the two accounts to be compared
    print_comparison(item_a, item_b)

    # Asking the user for an answer and checking if it is correct
    valid_answer = False
    while not valid_answer:
        answer = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
        if answer == "a":
            valid_answer = True
            game_over = check_answer(item_a, item_b)
        elif answer == "b":
            valid_answer = True
            game_over = check_answer(item_b, item_a)
        else:
            print("Invalid answer. Try again.")

    # Clear the screen
    os.system('cls')
    print(logo)

    if game_over == True:
        print(f"Sorry, that's wrong. Final score {score}.")
    else:
        score += 1
        print(f"You're right! Current score: {score}")
        item_a = item_b