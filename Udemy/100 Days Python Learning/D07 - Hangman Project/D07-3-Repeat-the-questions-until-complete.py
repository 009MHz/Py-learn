import random
# Todo 1: Randomizing the hidden word
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code for debugging
print(f'Pssst, the solution is {chosen_word}.')

# Todo 2: Converting jumlah text menjadi stripes
display = []
for stripes in chosen_word:
    display.append("_")

# Todo 4: Looping the prompt until there's no more stripes
game_over = False  # condition yg diberi jika scenario belum selesai
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Todo 3: Check the guess vs random word
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        game_over = True  # condition yang diminta untuk mengakhiri looping
        print("Game Over")


"""another approaches"""
# while "_" in display: #kondisi untuk looping jika masih ada stripes (teks kosong) pada kalimat yang diminta
#     guess = input("Guess a letter: ").lower()
#     for text_position in range(len(chosen_word)):
#         if guess == chosen_word[text_position]:
#             display[text_position] = guess
#     print(display)
#     if "_" not in display: #kondisi jika semua teks kosong (strip) sudah tidak ada lagi
#         print ("game Over")