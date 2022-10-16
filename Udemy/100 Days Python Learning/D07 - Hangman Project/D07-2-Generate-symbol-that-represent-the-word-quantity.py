import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
 
print(f'Solution is "{chosen_word}".') #test hasil random
 
display = [] #key untuk membuat list mendatar
 
for stripes in chosen_word:
  display.append("_") #command untuk menambahkan _ dalam []
print(display)
 
guess = input("Guess a letter: ").lower()
 
for text_position in range(len(chosen_word)): #key untuk menentukan posisi huruf yg ditebak pada kata yg diberikan
  if guess == chosen_word[text_position]: #command untuk menyaring benar tidaknya tebakan user dan merubahnya ke posisi yg tepat pada stripes yg dibuat
      display[text_position] = guess #command untuk mengubah strip (line 11) pada posisi yg tepat menjadi hasil tebakan user
 
print(display)