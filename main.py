import pandas


#TODO 1. Create a dictionary in this format:
nato_alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {value.letter: value.code for (letter, value) in nato_alpha_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter the sentence you want to check for: ").upper()
user_word_listed = [letter for letter in user_word]

user_word_nato_alpha = []
for letter in user_word_listed:
    if letter != " ":
        user_word_nato_alpha.append(nato_alphabet[letter])
    else:
        user_word_nato_alpha.append(" ")

print(f"Here are the nato alphabets: {user_word_nato_alpha}")
