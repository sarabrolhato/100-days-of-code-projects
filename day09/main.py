# The Secret Auction

# This program creates a secret auction where multiple bidders insert their name and bids, without knowing any of the previous bids.
# After all bids have taken place, the program announces the winner and the corresponding winning bid.

from os import system # We use this library to be able to clear the display using "system("cls")"
from IPython.display import clear_output # When using Jupyter Notebooks, we use "clear_output()" to clear the output of a cell

def find_highest_bidder(bidding_dictionary):
# Compare the bids in the dictionary
    winner = ""
    max_bid = 0
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > max_bid:
            winner = bidder
            max_bid = bidding_dictionary[bidder]
    
    print(f"The winner is {winner} with a bid of ${max_bid}.")


print("Welcome to the secret auction program.")

repeat = True
all_bids = {}

while repeat == True:
    # Ask the user for input
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    # Save data into dictionary
    all_bids[name] = bid

    # Check if new bids need to be added
    valid_input = False
    while valid_input == False:
        other_bidders = input("Are there any other bidders? Type 'yes'or 'no'. ")
        if other_bidders == "no":
            repeat = False
            valid_input = True
            system("cls")
            # clear_output(wait=False)
            # Call function to find the auction winner
            find_highest_bidder(all_bids)
        elif other_bidders == "yes":
            valid_input = True
            system("cls")
            #clear_output(wait=False)
        else:
            print("Invalid input. Type 'yes'or 'no'.")


# Using a max function to find the highest value and its corresponding key in a dictionary
#print(max(all_bids, key=all_bids.get))
#print(max(all_bids.values()))