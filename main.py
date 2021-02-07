import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
#print(data)

new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

user_letters = [letter for letter in user_input]

user_words = [new_dict[letter] for letter in user_letters if letter in new_dict]

print(user_words)



