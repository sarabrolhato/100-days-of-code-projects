# The Blackjack Capstone Project

import random
from os import system # We use this library to be able to clear the display using "system("cls")"


# List of existing cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Defining a function that checks if an ace was drawn, and counts it as 1 if the total sum of cards goes over 21
def check_for_aces(cards_list):
    sum_cards = sum(cards_list)
    if sum_cards > 21 and cards_list.count(11) > 0:
        cards_list[cards_list.index(11)] = 1
        return cards_list
    else:
        return cards_list

repeat_game = True # variable to loop game multiple times until user decides not to play anymore

# Game will be played multiple times until user chooses to exit
while repeat_game:

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "y":
        system("cls") # clear output

        game_over = False # variable to indicate when the game ends

        # Creating empty list of cards
        user_cards = list()
        computer_cards = list()
        # Creating sum of cards
        user_sum = 0
        computer_sum = 0
        
        # Deal both user and computer a starting hand of 2 random card values
        for i in range(0, 2):
            user_cards.append(random.choice(cards))
            check_for_aces(user_cards)
            user_sum += user_cards[i]
            
            computer_cards.append(random.choice(cards))
            check_for_aces(computer_cards)
            computer_sum += computer_cards[i]

        # After dealing the cards, reveal user's cards and computer's first card
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Detect when computer or user has a blackjack. If computer gets blackjack, then the user loses.
        if computer_sum == 21 or user_sum == 21:
            game_over = True
        else:  
            
            # If computer or user did not immediately get a blackjack, we ask the user if they want to draw another card
            # We repeat this step until the user busts, get a blackjack or decides to pass
            if not game_over:
                # Ask the user if they want to get another card
                # In each round, game ends immediately if user score goes over 21 or if the user or computer gets a blackjack
                # The user chooses to get another card until they bust, they get a blackjack or they decide to pass
                should_continue = True
                while should_continue:
                    user_get_card = input("\nType 'y' to get another card, type 'n' to pass: ")
                    if user_get_card == 'y':
                        user_cards.append(random.choice(cards))
                        check_for_aces(user_cards)
                        user_sum += user_cards[-1]
                        print(f"Your cards: {user_cards}, current score: {user_sum}")
                        if user_sum >= 21 :
                            should_continue = False
                            game_over = True
                        else:
                            # If game is not over, goes to next loop to ask if user wants to get another card
                            continue
                    else:
                        # User chose to pass. Exits loop but game is not over
                        should_continue = False
        
            # Once the user is done and no longer wants to draw more cards, let the computer play.
            # The computer should keep drawing cards unless their score goes over 16
            if not game_over:
                while computer_sum <= 16:
                    computer_cards.append(random.choice(cards))
                    check_for_aces(computer_cards)
                    computer_sum += computer_cards[-1]
        
        # At the end of the game, the final scores and the result are printed:
        print(f"\nYour final hand: {user_cards}, final score: {user_sum}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}\n")

        if computer_sum == 21:
            print("Computer has a Blackjack! Computer wins!")
        elif user_sum == 21:
            print("You have a Blackjack! You win! :D")
        elif computer_sum > 21:
            print("Opponent went over. You win! :D")
        elif user_sum > 21:
            print("Bust! You lose.")
        elif computer_sum > user_sum:
            print("Computer wins. You lose!")
        elif computer_sum == user_sum:
            print("It's a draw!")
        else:
            print("You win! :D")

    # If the user answers 'n' to start_game, the game does not start and prints "Goodbye"
    else:
        repeat_game = False
        print("Goodbye!")