import random 
hidden = random.randint(0,10)
print(f'The hidden number is "{hidden}"')

"""Using while loop to give the unlimited chances"""
while True:
    prompt = input('Do you want to play guess number game? (Y/n) ').lower()
    if prompt == 'n':
        break

    guess = int(input('Guess the number\n'))
    if guess < hidden:
        # 8   9
        if hidden - guess == 1:
            print("You're very close, try little bit higher")
        else:
            print("Your number is to small, try the higher number")
    elif guess > hidden:
        # 6     5
        if guess - hidden == 1:
            print("You're very close, try little bit lower")
        else:
            print("Your number is to high, try the lower number")
    else:
        if guess == hidden:
            print(f"Congratulations You Got it. The hidden number is {hidden}")
        else:
            print("I'll se you next time")


"""Using For loop to give the limited chances"""
print(f'\n\ntry to guess the number between 1-10 on 3 chances.\n')

# Todo 3: Returning message for each guessed chance
for chance in range(3):
    number = int(input("Take a guess.\n"))
    if number == hidden:
        print(f'Well done! You are correct on {(chance) + 1} attempt.')
        break #to break the loops when user guess the correct answer
    elif number < hidden:
        print("Your guess is too low!")
    elif number > hidden:
        print("Your guess is too high!")

if number != hidden: #message validation when user using all the chances
    print(
        f'The correct number is "{hidden}". '
        f'You lost your {(chance) + 1} chances.\nTry to re-run the games')