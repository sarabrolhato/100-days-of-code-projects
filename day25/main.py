# The US States Game

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Setting US Map as the background (turtle shape)
image = "blank_states_img.gif"
screen. addshape(image)
turtle.shape(image)

# Finding the x and y coordinates for each state (execute this without the exitonclick)
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

score = 0
correct_guesses = []

while score < 50:

    # Load states data
    with open("50_states.csv") as file:
        data = pd.read_csv(file)

    # Ask for user input
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state's name?").title()

    # Secret word for ending the game
    if answer_state == "Exit":
        # Generate csv file containing the states not guessed by the user
        # missing_states = []
        # for state in data["state"].unique():
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        missing_states = [state for state in data["state"].unique() if state not in correct_guesses]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Check if the guess is among the 50 states
    if (answer_state in data["state"].unique()) and (answer_state not in correct_guesses):
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.color("black")
        state_name.speed("fast")
        state_x = int(data[data["state"]==answer_state]["x"])
        state_y = int(data[data["state"]==answer_state]["y"])
        state_name.goto(state_x, state_y)
        state_name.hideturtle()
        state_name.write(f"{answer_state}", move=False, align="center", font=("Calibri", 12, "normal"))   

        score += 1
        print(score)
        correct_guesses.append(answer_state)
        print(correct_guesses)

        if score == 50:
            message_win = turtle.Turtle()
            message_win.penup()
            message_win.color("red") 
            message_win.goto(x=0,y=0)
            message_win.write("You win!", align="center", font=("Courier", 30, "normal"))
            message_win.hideturtle()
            