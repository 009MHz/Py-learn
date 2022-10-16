programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
#tujuan: hampir sama dengan kamus di dunia nyata, yaitu menyimpan beberapa informasi, baik command, maupun parameter ke dalam satu section / title
#format dictionary
# {Key: Value}
    #key: title / header dari dictionary yg kita inginkan
    #value: definition dari key yg kita setting
#programmer pada umumnya akan menuliskan format dictionary seperti ini:
programming_dictionary = { #open bracket lalu enter, untuk mempermudah membaca value yg kita berikan
    "Bug": "An error in a program that prevents the program from running as expected.", #untuk misahinnya cukup tambah "," di akhir code kemudian hit enter
    "Function": "A piece of code that you can easily call over and over again.",
    "Lorem": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
}#closing bracket, PERLU DIPERHATIKAN, untuk closing bracket tidak boleh maju indentationnya (harus sejajar dengan title awalnya)

##cara memanggil dictionary hampir sama dengan indexing list
    #list[1] => nama list[urutan data yang dipanggil]
    #dict[key] => nama kamus [nama title / key yg akan dipanggil]
print(programming_dictionary["Bug"]) #command untuk printing value dari Bug
print(programming_dictionary["Lorem"]) #maksudnya adalah printing dri value nya Tambah definisi lain, tapi pasti akan dapat error karena typo
##INGAT, banyak orang melakukan kesalahan di sini, jadi cek ulang key yg dipanggil supaya tidak ada typo ataupun hal lain sejenisnya, dan yang dipanggil haruslah sama persis seperti yg sudah didefinisikan di kamus sebelumnya, jika key nya string -> yg dipanggil harus pakai "", jika number, tidak perlu pakai, dsb.

#Menambah item ke dalam kamus
#nama kamus + [ key/title ] = value dari key yg diminta
programming_dictionary["True Love"] = "A hard thing to find"

#membuat kamus kosong (berguna untuk penggunaan looping dan if)
kosong = {}

#wipe an entire dictionary
#programming_dictionary = {} #bye bye all data

#editing a dictionary
# nama kamus + [ key/title yg sudah ada ] = new value / updated value
programming_dictionary["True Love"] = "Love to our Angela Sensei"
print(programming_dictionary) #output =  ngeprint semua + {} di awal dan akhir kalimat

#Loop through a dictionary
for key in programming_dictionary:
    print(key) #printing semua key nya kamus
    print(programming_dictionary[key]) #printing semua value tanpa {}