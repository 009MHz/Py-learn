#for loop
#command ini bertujuan untuk mengulangi sebuah siklus secara terus menerus
fruits = ["Apple", "Peach", "Pear"] #command ini berisikan "for"(nama command) fruit (variable baru untuk memanggil data yang akan #dipanggil) loop] "in" fruits (variable list data yang akan dipanggil utk di loop)
for fruit in fruits:
    print(fruit) #akan menulis semua data yang di dalam bracket [ ]
    print(fruit + " Pie") #akan menambah kata "pie" pada setiap data yang di loop
    print(fruits) #akan menulis data di belakang "=" dan di loop secara mentah-mentah 
    #namun jika indent nya dimundurkan, dia hanya akan menulis 1x
#semua data yang akan di loop akan menambah satu indent dibawah line for command