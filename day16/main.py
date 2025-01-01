# Build the coffee machine program using Object Oriented Programming (OOP)

# Program requirements:
# 1. Print report
# 2. Check is resources are sufficient
# 3. Process coins
# 4. Check if the transaction was successful
# 5. Make coffee

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initializing an object from the CoffeeMaker class
coffee_machine = CoffeeMaker()

# Initializing an object from the Menu class
menu = Menu()

# Initializing an object from the MoneyMachine class
money_machine = MoneyMachine()

machine_on = True

# The machine will keep asking customers for their orders until the machine operator turns it off
while machine_on:
    # Ask for the customer order and check if answer is valid: choose a drink, ask for a report or turn the machine off
    valid_answer = False
    while not valid_answer:
        customer_order = input(f"What would you like? ({menu.get_items()})").lower()
        if customer_order == "off":
            # Machine turns off
            valid_answer = True
            machine_on = False
            print("Turning off. Goodbye.")
        elif customer_order == "report":
            valid_answer = True
            # Print report of resources
            coffee_machine.report()
            money_machine.report()
        elif menu.find_drink(customer_order) != None:
            valid_answer = True
            # Create menu object with the ordered drink
            menu_item = menu.find_drink(customer_order)
        else:
            continue
    # If the client ordered a valid drink, the machine checks if resources are sufficient
    if machine_on == True and customer_order != "report":
        enough_resources = coffee_machine.is_resource_sufficient(menu_item)

        # If resources are sufficient, the machine asks for payment, process the coins, checks if payment is sufficient and gives the change
        if enough_resources == True:
            payment_accepted = money_machine.make_payment(menu_item.cost)

            # If payment is sufficient, the machine makes the coffee and updates the list of available resources
            if payment_accepted:
                coffee_machine.make_coffee(menu_item)