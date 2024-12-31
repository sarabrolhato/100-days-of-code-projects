# The coffee machine project
# The goal of this project is to build the program for a coffee vending machine.

# Program requirements:
# 1. The user chooses what drink they would like, or if they would like to see the report for the machine's resources.
# 2. The user can also choose to turn off the machine.
# 3. Based on the ordered drink, the machine checks if the available resources are available, and asks for payment.
# 4. The machine collects the payment.
# 5. The machine checks if the transaction was successful (total amount paid was enough to buy the chosen drink), and gives the change, if applicable.
# 6. Makes the coffee.
# 7. Updates the resources available (ingredients and money).
# 8. The machine asks for the order of the next customer until the machine is turned off.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Defining a function that prints a report of the available resources
def print_resources():
    """Prints the available resources in the coffee machine."""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

# Defining a function that checks if resources are sufficient for preparing the drink
def check_resources(drink):
    # """Returns True is resources are sufficient for preparing the selected drink, otherwise returns False."""
    # # Checks water
    # if resources["water"] < MENU[drink]["ingredients"]["water"]:
    #     print("Sorry, there is not enough water.")
    #     return False
    # elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
    #     print("Sorry, there is not enough coffee.")
    #     return False
    # # Checks milk
    # elif (drink != "espresso") and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
    #     print("Sorry, there is not enough milk.")
    #     return False
    # else:
    #     return True
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            return True

# Defining a function that collects coins from the customer and return the total amount paid
def collect_payment():
    """Returns the total amount from coins inserted by the user."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_amount = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return total_amount

# Defining a function that checks if the customer has paid more than the drink price and gives the corresponding change
def give_change(drink, total_amount):
    """Calculates the amount of change due."""
    if total_amount > MENU[drink]["cost"]:
        change = total_amount - MENU[drink]["cost"]
        print(f"Here is ${change} in change.")

# Defining a function that updates the list of available resources after a drink is made
def update_resources(drink):
    """Updates the list of available resources after a drink is made."""
    resources["money"] += MENU[drink]["cost"]
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


# While the machine is on, the machine will ask for the customer's order
machine_on = True
while machine_on:
    # Ask for the customer order and check if answer is valid: choose a drink, ask for a report or turn the machine off
    valid_answer = False
    while not valid_answer:
        customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if customer_order == "report":
            valid_answer = True
            # Print report of resources
            print_resources()
        elif customer_order == "off":
            valid_answer = True
            # Machine turns off
            machine_on = False
            print("Turning off. Goodbye.")
        elif (customer_order == "espresso") or (customer_order == "latte") or (customer_order == "cappuccino"):
            valid_answer = True
        else:
            print("Invalid answer. Please type a valid order.")

    # If the customer ordered a drink, the machine checks if resources are sufficient
    enough_ingredients = False
    if machine_on == True and customer_order != "report":
        enough_ingredients = check_resources(customer_order)

        # If the resources are sufficient, the machine asks for payment
        if enough_ingredients == True:
            # Ask for money and collect the payment
            total_paid = collect_payment()
            # If the money if enough to pay for the drink, give change (if any) and make the drink
            if total_paid >= MENU[customer_order]["cost"]:
                # Give change, if applicable
                give_change(customer_order, total_paid)
                # Make the drink
                print(f"Here is your {customer_order} ☕ Enjoy!")
                # Deduct resources
                update_resources(customer_order)
            else:
                # If amount paid is less than the price of the drink, money is returned
                print("Sorry, that's not anough money. Money refunded.")
