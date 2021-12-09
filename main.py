import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv").to_dict()
nato_dict = {row.letter:row.code for (index, row) in pandas.DataFrame(data).iterrows()}
def retry_nato():
    word_input = input("Enter the word: ").upper()
    try:
        phonetics = [nato_dict[letter] for letter in word_input]
    except KeyError:
        print("Sorry, only use letters in the alphabet")
        retry_nato()
    else:
        print(phonetics)
retry_nato()
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

