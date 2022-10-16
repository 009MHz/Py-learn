import random #INI JEBAKAN, karena instruksinya tidak boleh change code above, sementara import random harus berada di paling atas
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names[])
#pada tahap ini kita tidak bisa merandom string secara mentah2, oleh karena itu kita perlu menggunakan command len() untuk mengganti string menjadi urutan angka
name_convert = len(names) #untuk merubah nama menjadi urutan angka
lucky_number = random.randint(0, name_convert - 1) #command untuk merandom angka yang akan keluar dan nantinya akan dirubah menjadi string lagi
lucky_boss = names[lucky_number] #command untuk merubah gacha angka menjadi name
print(lucky_boss + " is going to buy the meal today.")



