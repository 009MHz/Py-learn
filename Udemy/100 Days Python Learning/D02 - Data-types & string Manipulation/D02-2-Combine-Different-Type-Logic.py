char_num = len(input("What is your name? "))
# print("Your name has " + char_num + "characters.")
# print(type(char_num))
# command "type()" digunakan untuk mengetahui jenis data apa yang dipakai dalam variable yang dipanggil
#coding pada line 3 akan mengalamai error result karena tipe data bukan string melainkan integer
char_num_upd = str(char_num)
#untuk mengatasi error tersebut bisa menggunakan cara di line 6, yaitu buat variable table baru -> char_num_upd yang mengambil data dari char_num setelah dikonversi ke string -> str(char_num)
print("Your name has " + char_num_upd + " characters.")
  #f-string
#digunakan untuk menyatukan semua jenis data (boolean, integer, float, string) dengan format seperti ini
score = 0 #int
height = 1.71 #float
isWinning = True #boolean
print(f"your score is {score}, your height is {height}, you are the {isWinning} victorious") #command(f"diikuti string, kemudian call data yang akan diinput dengan {} tutup dengan")