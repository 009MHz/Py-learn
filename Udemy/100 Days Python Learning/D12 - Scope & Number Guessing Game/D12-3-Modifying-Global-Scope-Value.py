"""Modifying Global Scope"""
enemies = 1

#case 1: Invalid
def increase_enemies():
    enemies += 1
    print(f"enemies inside function: {enemies}")
#karena memanggil global scope dari local scope yg secara teori unreachable

#case 2: bikin variable baru (dari global) dalam local scope
def increase_enemies():
    enemies = 0
    enemies += 1
    print(f"enemies inside function: {enemies}")
#harus mencari value yang akan dimodif, kemudian dimasukkan ke dalam local scope, baru dimodif (+1) di dalam local fungsi nya

#case 3: menambahkan "global" dan value yg diambil ke dalam local scope
def increase_enemies():
    global enemies
    enemies += 1
#kedua line diatas merupakan essential requirements karena tanpa ditambahkannya kedua code, kita tidak akan bisa menjalankan fungsi baru yg akan kita buat
    print(f"enemies inside function: {enemies}")

#case 4: menggunakan return function
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1 #mengembalikan value dari global scope kemudian modify di dalam new function
#approach ini paling mendekati tujuan karena kita tidak mengganggu apapun dari global scope nya
#namun kita perlu mendefine param baru untuk memanggil global value + menggunakan fungsi yg dibuat
enemies = increase_enemies() #param baru untuk memanggil global value + value setelah modifikasi 
print(f"enemies outside function: {enemies}")

"""Hati hati dalam melakukan perubahan pada Global Value (enemies). Karena kita belum tau dimana posisi value tersebut disimpan dan bisa terlompati banyak line sekaligus. Let say kita udah coding sampai line 200, dan global valuenya di line 3. Oleh karena itu case 3 & 4 adalah approach yg lebih disarankan."""