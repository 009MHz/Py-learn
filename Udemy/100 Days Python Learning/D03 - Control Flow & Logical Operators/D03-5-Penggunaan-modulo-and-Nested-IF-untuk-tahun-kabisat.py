# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
mod4 = year % 4
mod100 = year % 100
mod400 = year % 400
if mod4 == 0:
  print("This is Leap year")
elif mod100 == 0:
  print("This is Leap year")
elif mod400 == 0:
  print("This is Leap year")
else:
  print("This is not Leap year")
#atau bisa juga dengan cara yang lain seperti ini
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Tahun Kabisat")
    else:
      print("Bukan Kabisat")
  else:
    print: ("Tahun Kabisat")
else:
  print("Bukan Kabisat")
  


