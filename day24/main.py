# Given a list of invited names and a sample invitation letter,
# Generate a file for each invited person named "letter_for_[name].txt", with the invitation letter
# Substituting the "[name]" in the sample invitation letter for the person's name.

with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in name_list:
    name = name.strip()
    with open("Output/ReadyToSend/letter_for_" + name + ".txt", "w") as file:
        file.write(letter.replace("[name]", name))


