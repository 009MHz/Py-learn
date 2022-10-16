# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split() #command supaya input bisa >1 & dipisahkan dengan spasi
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#cara cepat
#jumlah_tinggi = sum(student_heights) #penjumlahan langsung semua tinggi
#jumlah_orang = len(student_heights) #penghitungan langsung data
#average = round(jumlah_tinggi / jumlah_orang) #rumus rata-rata
#print(average) #munculkan

#maksud pealajaran kali ini:
total_height = 0 #kunci variable untuk menjumlahkan semua data yang diinput (supaya bisa di loop satu-satu)
for height in student_heights: #habis command for boleh random, asal jelas supaya tidak ketuker, yang ga boleh, data habis "in" nya
  total_height = total_height + height #command singkatnya total_height =+ height
  #maksud command di atas adalah (0+ data ke 1) & (0+data ke 2) dst
print(total_height) #indent sengaja dimundurkan supaya penjumlahan berjalan, jika tidak dimundurkan maka looping akan berjalan dan hasilnya akan menjumlahan secara fibonacci sampai semua data habis

number_of_students = 0
for students in student_heights:
  number_of_students += 1 #maksudnya adalah command ini akan mengeksekusi (0+1) & (0+1) sampe semua data yg diinput habis
print(number_of_students)

average = total_height / number_of_students #baru setelah ekstraksi coding selesai, nanti dicari average nya
print(round(average))
