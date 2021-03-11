import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")


new_dict = {row.letter:row.code for (index,row) in data.iterrows()}

incorrect_input = True
while incorrect_input:
    user_input = input("Enter a word: ").upper()
    try:
        user_words = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
    else:
        print(user_words)
        incorrect_input = False



