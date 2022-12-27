import pandas as pan

data = pan.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format: {'A': 'Alfa', 'B': 'Bravo', ...}
NATO = {}
for index,rows in data.iterrows():
    NATO[rows.letter] = rows.code

print(NATO)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def phonetic_convert(text):
    # Breakdown passable text into separated letter & excluding whitespaces
    br_dwn = []
    for x in text:
        if not x.isspace():
            br_dwn.append(x)
    print(br_dwn)

    # Checking each iterated text availability inside the dictionary
    output = []
    for x in br_dwn:
        if x in NATO[x]:
            output.append(NATO[x])

    return output


print(phonetic_convert(text=input("Enter your text:\n").upper()))
