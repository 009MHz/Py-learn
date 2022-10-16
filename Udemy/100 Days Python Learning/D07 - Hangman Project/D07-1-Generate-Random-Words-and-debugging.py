#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
pilihan = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
clue = input("Guess the letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in (pilihan): #looping huruf di pilihan kalimat
    if letter == (clue): #condition apabila tebakan huruf benar / salah seperti yg tercantum di pilihan kalimat
        print("Yes")
    else:
        print("No")