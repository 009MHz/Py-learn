# MISSION: looping the calculation
from replit import clear
# calculator function
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
#math operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(): #9 recursion, berfungsi untuk mengulangi semuanya dari awal (dari input num1) setelah user mengakhiri sessi sebelumnya seperti di nomor 8 {looping dalam loop}
    #user interaction
    num1 = int(input("What's the first number?: ")) #1 mengeluarkan input ini dari looping karena user hanya perlu untuk memberikan input selanjutnya instead input dari awal
    
    calculation = True #2 variable kunci utk looping
    while calculation:
        operation_symbol = input("Pick an operation: ") #3 start looping, yaitu proses input operation simbol
        num2 = int(input("What's the next number?: ")) #4 next looping, input nomor selanjutnya, dan ketika ini di looping akan tetap berfungsi sebagai num 2 (bukan num 3,4 dst) karena num 1 sudah dikeluarkan dari looping (liat no7)
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        proceed = input(f'"Type "y" to continue calculate with {answer}, type "n" to exit\n') #5 validasi user untuk melanjutkan kalkulasi  / tidak
        if proceed == "y": #6 setting kondisi jika user lanjut
            num1 = answer #7 jika lanjut, jawaban user sebelumnya akan menggantikan num1 yang dikeluarkan dari looping supaya num1 meneruskan jawaban user terakhir instead angka sewaktu starting
        else:
            calculation = False #8 kondisi untuk mengakhiri sessi kalkulator yang ada
            calculator() #10 jika tidak memanggil fungsi ini di kondisi else, maka sesi akan benar-benar berakhir tanpa bisa menggunakan fungsi kalkulator untuk sessi selanjutnya
calculator() #11 jika tidak memanggil fungsi ini di luar definisi fungsi yang diberikan (dari num1 - proceed) maka kalkulator tidak akan bisa dijalankan, karena fungsi nya cuman diberikan tapi tidak digunakan