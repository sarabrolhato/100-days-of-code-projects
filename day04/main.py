# Rock Paper Scissors

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

moves = [rock, paper, scissors]

# user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

valid_move = False
while not valid_move:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user >= 0 and user < 3:
        print(f"You chose: \n{moves[user]}")
        valid_move = True
    else:
        print("Invalid answer. Try again.")

print(f"Computer chose: \n{moves[computer]}")

if user == computer:
    print("Draw. Try again.")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You win!")
elif user >= 3 or user < 0:
    print("You typed an invalid number. You lose.")
else:
    print("You lose.")