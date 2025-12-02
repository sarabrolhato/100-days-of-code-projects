import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(dict)
print(dict["A"])

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_valid = False

while not is_valid:
    word = input("Please enter a word:")

    try:
        phonetic_word = [dict[letter.upper()] for letter in word]
        is_valid = True
        print(phonetic_word)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")