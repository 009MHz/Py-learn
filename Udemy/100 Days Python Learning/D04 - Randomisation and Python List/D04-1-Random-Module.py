#Random Module: contohnya dapat dilihat di sini -> https://www.askpython.com/?s=random+module
#digunakan untuk RNG / gacha dalam suatu game jika menggunakan python sebagai tool nya
import random
random_integer = random.randint(1, 10) #command untuk merandom angka dari 1-10
print(random_integer)
#dalam module ini kita bisa memanggil file lain dalam folder ini e.g: isi dari RNG.py

random_float = random.random() #random command ini hanya bisa dipakai untuk angka 0 - 0.99
print(random_float)
#untuk membuat random float berisi angka >1, bisa menggunakan rumus aljabar seperti ini
random_big_Float = random.random() * 5
print(random_big_Float)
