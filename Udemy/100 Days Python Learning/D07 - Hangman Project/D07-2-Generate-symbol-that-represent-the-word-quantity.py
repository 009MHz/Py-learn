import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Solution is "{chosen_word}".')  # help for debugging

display = []  # key untuk membuat list kosong sebelum diconvert menjadi jumlah strip
for x in chosen_word:
    # iterating the text
    display.append("_")
    # adding '_' into list sebanyak passed word
print(display)

guess = input("Guess a letter: ").lower()

for text_position in range(len(chosen_word)):
    # converting choosen word menjadi range (sejumlah text yg diberikan)
    # iterating text menjadi urutan index pada substring
    if guess == chosen_word[text_position]:
        # calling text yg terandom menggunakan substring iteration
        # verify passed character based on substring iteration
        display[text_position] = guess
        # converting strip menjadi text jika guess user ada dalam substring iteration
print(display)
