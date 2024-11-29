# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give (%)? 10, 12, or 15?"))
n_people = int(input("How many people to split the bill?"))

total = (bill + ((bill*tip_percent)/100))
total_per_person = round(total / n_people, 2)

# print(f"Each person should pay: ${total_per_person}") # This solution does not print the full number with 2 decimal places when there are zeros.

# Print total per person with two decimal places
print(f"Each person should pay: ${total_per_person:.2f}")