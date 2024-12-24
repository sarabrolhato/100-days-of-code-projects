# The Number Guessing Game

# This is the solution suggested in the course, using functions to execute all parts of the game.

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS

def game():
    # Starting Game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number between 1 and 100
    chosen_number = random.randint(1, 100)
    
    # Set difficulty level
    turns = set_difficulty()
    
    # Let the user make a guess
    guess = 0
    while turns != 0 and guess != chosen_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, chosen_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")


game()