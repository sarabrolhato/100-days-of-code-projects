# Escaping the Maze

# This is the solution to the "Maze" Challenge on Reeborg's World:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Finding a wall to begin
while not wall_on_right():
    if front_is_clear():
        while front_is_clear():
            move()
    else:
        turn_left()
    
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        while front_is_clear() and wall_on_right():
            move()
    elif front_is_clear()==False:
        while front_is_clear()==False:
            turn_left()