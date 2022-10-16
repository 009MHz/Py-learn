#input("What is your name?")
# name = input("What is your name? ") "name" digunakan sebagai variable A
# print(name) -> command dipakai untuk mengambil data dari variable A (hasil dari line 2)dan tidak perlu melakukan penulisan satu per satu

name = "Hazeya"
print(name)

name = "Renata"
print(name)

print(len(input("What is your name? ")))

name = "Jack"
print(name)

name = "Angela"
print(name)


#dari function ini print(len(input("What is your name? ")))
#bisa dipersingkat menjadi beberapa variable seperti di bawah
name = input("What is your name?") #name=variable A
length = len(name) #length=variable B dan command len menghitung jumlah dari (variable A)
print(length) #dan yang terakhir akan menulis dari variable B
#berbeda dari code yang dijejer sekaligus, code type ini akan mengeksekusi order dari atas ke bawah bisa digunakan ketika code yang ditulis terlalu banyak