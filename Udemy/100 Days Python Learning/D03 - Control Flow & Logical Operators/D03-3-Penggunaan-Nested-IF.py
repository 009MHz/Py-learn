#Nested if / else: merupakan chain link atau koneksi berurutan yang tidak hanya memakai 2 syarat ya dan tidak, namun bisa ada beberapa opsi setelah ya dan tidak
#   jika if adalah command untuk 2 opsi ya dan tidak elif <else if> merupakan opsi untuk ya1 & ya2 sebelum dieksekusi sebagai tidak
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can get in!")
  age = int(input("How old are you? "))
  if age < 12:
    print("You need $5 kid")
  if age <= 18:
    print("You're a kid, you need $7 to get in")
  else:
    print("$12 should be OK")
else:
  print("Go back next time Kid!")