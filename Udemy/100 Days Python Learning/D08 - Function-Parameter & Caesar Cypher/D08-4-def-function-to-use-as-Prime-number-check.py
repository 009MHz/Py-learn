#Write your code below this line 👇
def prime_checker(number):
    prime = True #variable untuk menentukan apakah angka yang dicari prime or not
    for check in range(2,number): #looping angka yang dicari dengan start 2 (i.e: 2 - 97), karena prime number pasti bisa dibagi 1
        if number % check == 0 : #nomor yang diinput / looping nomor yang dicari (97/2, 97/3,...97/96) dan tidak mengikutkan bilangan itu sendiri
            prime = False #kondisi yang diberikan jika bukan prime number, karena semua bilangan prima harus sisa 1 jika menggunakan modulo
    if prime:
        print ("It's a prime number.") #kondisi ditarik satu indent supaya outputnya tidak print satu satu sampai nomor yang dicari
    else:
        print("It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



