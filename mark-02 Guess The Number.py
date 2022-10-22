# Todo 1: Randomizing the number
import os
import random

secrets = random.randint(1, 10)
# print(f'The secret number is "{secrets}".')

# Todo 2:  Ask the player to guess the number
name = input("What should I call you? ")
print(f'Hi "{name}", try to guess the number between 1-10 on 3 chances.\n')

# Todo 3: Returning message for each guessed chance
for chance in range(3):
    guess = int(input("Take a guess.\n"))
    if guess == secrets:
        print(f'Well done "{name}"! You are correct on {(chance) + 1} attempt.')
        break #to break the loops when user guess the correct answer
    elif guess < secrets:
        print("Your guess is too low!")
    elif guess > secrets:
        print("Your guess is too high!")
if guess != secrets: #message validation when user using all the chances
    print(
        f'Sorry "{name}". '
        f'The correct number is "{secrets}". '
        f'You lost your {(chance) + 1} chances.\nTry to re-run the games')