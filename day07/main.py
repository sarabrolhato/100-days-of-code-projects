# Hangman - Country Names

# This project creates a hangman game for guessing country names.
# The code has been adapted from the course solution to successfully deal with capital letters and country names with multiple words.

import random

# Importing custom modules
import day7_hangman_art
import day7_hangman_words 

print(day7_hangman_art.logo)

# Randomly choose a work from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(day7_hangman_words.word_list)

# Create a placeholder with the same number of blanks as the chosen word
placeholder = ""
for position in chosen_word:
    if (position == " ") or (position == "-") or (position == "'"):
        placeholder += position
    else:
        placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

# Create a variable called 'lives' to keep track of the number of lives left
lives = 6

# Use a while loop to let the user guess again
while game_over == False:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    display = ""
    
    if guess in correct_letters:
        # If the user has entered a letter they've already guessed, print the letter and let them know. We should not deduct a life for this.
        print(f"You have already guessed {guess}. Try again.")
    elif guess in incorrect_letters:
        # If the user has entered an incorrect letter that they have already typed, print the letter and let them know. We should not deduct a life for this.
        print(f"You have already typed {guess}. Letter {guess} is not in the word. Try again.")
    else:
        # Create a display that puts the guess letter in the right place.
        # The display should print the current guess along with previous correct letters.
        for letter in chosen_word:
                if (letter == guess) or (letter == guess.upper()):
                    display += letter
                    correct_letters.append(guess)
                elif (letter in correct_letters) or (letter.lower() in correct_letters):
                    display += letter
                elif (letter == " ") or (letter == "-") or (letter == "'"):
                    display += letter
                else:
                    display += "_"
    
        print(display)
    
        if (guess not in chosen_word) and (guess.upper() not in chosen_word):
            # If guess is not a letter in the chosen_word, then reduce lives by 1.
            lives -= 1
            incorrect_letters.append(guess)
            # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                game_over = True

        if "_" not in display:
            # The user wins when they have correctly guessed all the letters.
            game_over = True
            print("You win!")
        elif game_over == True:
            # If lives goes down to 0, then the game should stop and it should print "You lose".
            print(f"The word was {chosen_word}. You lose.")
        else:
            # If the game is not over yet, print the ASCII art from 'stages' that corresponds to the current number of lives the user has remaining.
            print(day7_hangman_art.stages[6 - lives])
            # Tell the user how many lives they have left.
            print(f"You have {lives}/6 lives left.")