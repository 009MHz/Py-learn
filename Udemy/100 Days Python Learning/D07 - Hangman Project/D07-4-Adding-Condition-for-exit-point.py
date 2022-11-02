# Todo 5: Adding the scenario for user attempts to guess the word
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
lives = 6

# Todo 1: Randomizing the hidden word
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code for debugging
print(f'Pssst, the solution is {chosen_word}.')

# Todo 2: Converting jumlah text menjadi stripes
display = []
for stripes in chosen_word:
    display.append("_")

# Todo 4: Looping the game
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Todo 3: Check the guess vs randomed word
    for x in range(word_length):
        letter = chosen_word[x]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[x] = letter
    print(display)

    # Todo 5a: reducing the lives
    if guess not in chosen_word:
        '''indent level code ini harus sejajar dengan line 83 agar tidak nge run berkali kali sejumlah huruf 
        pada kata yang diambil'''
        lives -= 1
        print(f" You have {lives} lives remaining")

        # Todo 5b: ending the game using second exit point
        if lives == 0:  # syarat untuk mengakhiri game
            end_of_game = True  # kondisi spesifik untuk mengakhiri looping
            print(f'"Game Over"\nThe Correct Word is "{chosen_word}"')

    if "_" not in display:
        end_of_game = True  # exit condition pertama
        print("You Win")

    # Todo 6: print out the stages that represent to user's attempt
    print(stages[lives])