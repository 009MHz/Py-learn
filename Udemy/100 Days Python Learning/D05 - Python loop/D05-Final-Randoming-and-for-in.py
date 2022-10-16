 #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = "" #untuk mengubah key input menjadi empty string
for huruf in range(1, nr_letters +1): #semisal 4 angka maka akan diambil 1-4 instead 1-3
   password += random.choice(letters)
  #password = kosong, makanya pakai += untuk menambahkan random input dari variable letters supaya password = randoman letters
  
for sym in range(1, nr_symbols +1):
  password += random.choice(symbols)
  
for angka in range(1, nr_numbers +1):
  password += random.choice(numbers)
  
print(f"Your password will be:\n{password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = [] # key untuk mengubah input jadi list

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters)) #apppend digunakan karena tidak bisa memakai code yang sama dengan sebelumnya (input adalah list instead of string)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list) #output di dode ini masih berwujud list

password = "" 
for char in password_list:
  password += char
#code di atas ini merupakan converter dari list ke string
print(f"Your password is: {password}")