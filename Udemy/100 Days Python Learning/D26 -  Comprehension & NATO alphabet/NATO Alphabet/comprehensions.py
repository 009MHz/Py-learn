import pandas as pan

data = pan.read_csv("nato_phonetic_alphabet.csv")

# 1. Create a dictionary in this format: {'A': 'Alfa', 'B': 'Bravo', ...}
NATO = {y.letter: y.code for (x, y) in data.iterrows()}
# print(NATO)

#2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic_convert(text):
    # Breakdown passed text into separated letter & excluding whitespaces
    br_dwn = [x for x in text if not x.isspace()]
    # print(br_dwn)

    # Checking each iterated text availability inside the dictionary
    output = [NATO[x] for x in br_dwn if x in NATO[x]]
    return f"\nPhonetic Alphabet result:\n{output}"


print(phonetic_convert(text=input("Enter your text:\n").upper()))
