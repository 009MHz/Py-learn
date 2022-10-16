#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for stripes in chosen_word:
  display.append("_") 

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
game_over = False #situasi yang diminta untuk melakukan looping input di bawah ini
while game_over:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    print(display)
    if "_" not in display:
        game_over = True #situasi yang diminta untuk mengakhiri looping
        print("Game Over")
# #another approaches
# while "_" in display: #kondisi untuk looping jika masih ada stripes (teks kosong) pada kalimat yang diminta
#     guess = input("Guess a letter: ").lower()
     
#     for text_position in range(len(chosen_word)): 
#         if guess == chosen_word[text_position]: 
#             display[text_position] = guess 
#     print(display)
#     if "_" not in display: #kondisi jika semua teks kosong (strip) sudah tidak ada lagi
#         print ("game Over")