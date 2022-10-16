#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3" 

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

from replit import clear
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(texting, shifting, directioning):
    crypt_text = ""
    for letter in texting:
      if letter in alphabet: #key utk memriksa user input apakah berada dalam list alphabet
          pos = alphabet.index(letter)
          if direction == "encode":
              new_pos = pos + shifting
              while new_pos >= 26: #key untuk converting jika teks yang dirubah berada diluar jangkauan list index
                  new_pos -= 26
          elif direction == "decode":
              new_pos = pos - shifting
              while new_pos <0: #key untuk converting jika teks yang dirubah berada diluar jangkauan list index
                  new_pos += 26
          crypt_text += alphabet[new_pos]
      else: #key untuk mengembalikan semua input (symbol / angka) jika bukan teks
        crypt_text += letter
    print(f'The {direction}d result: "{crypt_text}"\n')

from art import logo
print(logo)

hop = False #key awal untuk memulai looping command input
while not hop: 
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(texting = text, shifting = shift, directioning = direction)
    restart = input('Type "Yes" if you want to run again, type "No" if you decide to stop?\n').lower()
    clear() #additional key untuk membersihkan previous logs
    if restart == "no":
        hop = True #key  untuk mengakhiri looping command input
        print("\nI'll see you next time")

