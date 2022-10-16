import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hand_sign = [rock, paper, scissors]

user_choice = int(input("Jankenpon! 0 for Rock, 1 for paper, and 2 for scissors\n"))
if user_choice >=3 or user_choice <1 :
  print("Invalid number, it's bot victory") 
#akan ada bug jika user memilih angka >3 karena list index hanya 0,1,2, oleh karena itu code if+else harus berada tepat dibawah line 32 supaya tidak mengeksekusi line 37 dulu
else: #kemudian semua line dibawah ini diselect dan dimajukan satu tab supaya elif dibawah dapat berfungsi kembali
  print(f"You choose \n{hand_sign[user_choice]}") 
#hand sign = 0,1,2 user choice=memanggil urutan yang diinput
  
  bot = random.randint(0, 2)
  print(f"AI choose \n{hand_sign[bot]}")
  
  if user_choice == bot:
    print ("It's a draw, try again next time")
  elif user_choice == 2 and bot == 0:
    print("Sorry, You lose with bot")
  elif user_choice > bot:
    print("You win, congrats!!")
  elif user_choice < bot:
    print("Loser")