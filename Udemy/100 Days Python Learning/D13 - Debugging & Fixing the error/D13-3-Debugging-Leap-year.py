year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#1 untuk cek data type bisa menggunakan command ini di console nya / terminal (VS code):
    # type(data variable yang dipanggil)
    # type(year)