#ForIn command untuk game FizzBuzz
#Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #if statement akan berhenti sekali dia dapat argument yang true, jadi misal line ini di paling bawah, nama fizzbuzz tidak akan muncul karena angka/3 or angka/5 sudah muncul duluan, sedangkan code gabungan ini harus dieksekusi duluan sebelum yang lain
    print("Fizzbuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)