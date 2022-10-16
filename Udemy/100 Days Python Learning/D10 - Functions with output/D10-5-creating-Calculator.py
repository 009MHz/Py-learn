#1 creating math operation
#1b return langsung dipakai karena fungsi def() harus punya definisi dari fungsinya

#penjumlahan
def add(n1,n2):
    return n1 + n2 

#pengurangan
def min(n1,n2):
    return n1 - n2

#perkalian
def multip(n1,n2):
    return n1 * n2

#pembagian
def divid(n1,n2):
    return n1 / n2

#2 membuat kamus untuk memanggil fungsi math_ops
    #key = symbol math operation, value = nama fungsi
math_op = {
    "+" : add,
    "-" : min,
    "*" : multip,
    "/" : divid
}

#3 membuat teks untuk meminta input user
num1 = int(input("What's the first number?\n"))


#4 input user interaction
    #hal yg perlu diperhatikan kamus math_op harus terpanggil based on user input
user_op = input('Select the operation, "+", "-", "*" or "/"\n')
num2 = int(input("What's the second number?\n"))
calc = math_op[user_op] #5 membuat command baru untuk memanggil fungsi di kamus yang kemudian memanggil fungsi def() yang dibuat sebelumnya based on user input
result = calc(num1, num2) #6 command untuk prosesing user input pada calculator yg bersangkutan
    
print(f' {num1} {user_op} {num2} = {result}')