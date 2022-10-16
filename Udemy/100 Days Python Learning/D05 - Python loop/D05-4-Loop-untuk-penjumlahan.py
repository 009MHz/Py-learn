#Menjumlahkan angka dengan ForIn dalam range
#Write your code below this row 👇
summary = 0
for number in range(0, 102, 2): #memanggil semua data di antara 0 - 102 (kecuali 0 & 102) dengan kelipatan 2 angka
  #print(number)
  summary += number # 0+angka dari line 4, ex: (0+2)+(0+4). . .(0+100)
print(summary)

#atau bisa juga dengan cara berikut

# alternative_sum = 0
# for number in range(1, 101):
#   if number % 2 == 0:
#     # print(number)
#     alternative_sum += number
# print(alternative_sum)