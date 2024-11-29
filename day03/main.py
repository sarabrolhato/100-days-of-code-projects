# Treasure Island - A choose your own adventure game

print("Welcome to Treasure Island. Your mission is to find the treasure.")
left_right = str.lower(input('You\'re at a cross road. Where do you want to go? Type "left" or "right".'))

if left_right == "left":
    swim_wait = str.lower(input("You've come to a lake. There is as island in the middle of the lake. "
                                "Type \"wait\" to wait for the boat. Type \"swim\" to swim across."))
    if swim_wait == "wait":
        door = input("You arrive at the Island unharmed. There is a house with 3 doors. "
                     "One red, one yellow, and one blue. Which color do you choose?").lower()
        if door == "yellow":
            print("You found the treasure! You win!")
        elif door == "blue":
            print("You enter a room of beasts. Game over.")
        elif door == "red":
            print("It's a room full of fire. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")