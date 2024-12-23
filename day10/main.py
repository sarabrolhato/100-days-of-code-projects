# The Calculator Project

from os import system # We use this library to be able to clear the display using "system("cls")"
from IPython.display import clear_output # When using Jupyter Notebooks, we use "clear_output()" to clear the output of a cell

# Write out the 4 functions: add, subtract, multiply and divide.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Add these 4 functions into a dictionary as the values. Keys are "+", "-", "*" and "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

should_continue = True
new_number = True
while should_continue:
    if new_number == True:
        number1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    calculator_function = operations[operation]
    result = calculator_function(n1=number1, n2=number2)
    print(f"{number1} {operation} {number2} = {result}")
    repeat = input("Do you want to perform another calculation? Type 'yes' or 'no': ")
    if repeat == 'no':
        should_continue = False
        print("Goodbye")
    else:
        reuse_n1 = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation: ")
        if reuse_n1 == "y":
            new_number = False
            number1 = result
        else:
            new_number = True
            system("cls")