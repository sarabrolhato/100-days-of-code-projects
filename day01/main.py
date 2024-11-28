# Band Name Generator

print("Welcome to the Band Name Generator.")

# Ask for the name of user's city
city = ""
while city == "":
    city = input("What's the name of the city you grew up in?\n")
    if city == "":
        print("Invalid input. Please try again.")

# Ask for user's pet name
pet_name = ""
while pet_name == "":
    pet_name = input("What's your pet's name?\n")
    if pet_name == "":
        print("Invalid input. Please try again.")

print("Your band name could be " + city + " " + pet_name)