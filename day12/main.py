# The Number Guessing Game

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate random number between 1 and 100
chosen_number = random.randint(1, 100)

# Select difficulty level
should_continue = True
while should_continue:
    # Let the user guess a number
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        attempts = 5
        should_continue = False
    elif difficulty == "easy":
        attempts = 10
        should_continue = False
    else:
        print("Invalid input.")
        
print(f"You have {attempts} attempts remaining to guess the number.")

# Checking guesses and keeping track of attempts left
game_over = 0
while attempts > 0 and game_over == 0:
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
        game_over = 1
    elif guess > chosen_number:
        print("Too high.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    else:
        print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")

if attempts == 0:
    print("You've run out of guesses, you lose.")