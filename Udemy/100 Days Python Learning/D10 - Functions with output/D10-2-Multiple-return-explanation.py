#next def() method dengan menggunakan return
#return logic 1
# def format_name(f_start,l_start):
#     f = f_start.title()
#     l = l_start.title()
#     return f'{f} {l}' #2 command ini merupakan penutup untuk definisi fungsi yg diminta
#     print("Command after return") #1 code ini tidak akan pernah ter eksekusi karena berada di bawah command "return", sedangkan return merupakan command untuk mengakhiri sebuah fungsi
# print(format_name("hARiS","SATRIYo"))
    
#2 penggunaan return logic yg salah
def form_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs." 
      #1 return akan mengembalikan value dari line 12 yaitu empty string (baik di input yg pertama ataupun yg kedua) dengan memberikan output berupa string yg ditulis setelah return
      #2 return akan memberikan output "none" jika user memberikan value yang sesuai yakni semua input yg diminta dan memberikan none karena semua requirements dari input yg diminta sudah dipenuhi
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    f"Logic 2 example Result: {formated_f_name} {formated_l_name}" 
    #3 Fungsi ini akan ber output as
        #"none" jika user mengisi perintah input dan memanggil output yg diminta
        # "You didn't provide valid inputs." jika user tidak mengisi output
    #karena berada di bawah command return yg merupakan perintah penutup setelah command .title() dieksekusi
    
#untuk memanggil & verifikasi code yg dibuat, bisa menggunakan cara seperti berikut

    #Storing output in a variable
formatted_name = form_name(input("Your first name: "), input("Your last name: "))
print(f'"Type 1 print test result "{formatted_name}""')
    #or printing output directly
print(
    form_name(
        input("What is your first name? "),input("What is your last name? ")))
    #4 Akan mencetak output berupa none atau "You didn't provide valid inputs." seperti output yg dihasikan dari point 3 

#3 Multiple return Logic yg benar
def name_convert(f0, l0):
    if f0 == "" or l0 == "":
        return "You didn't provide valid inputs." #1 format return pengganti result if statement
    f1 = f0.title()
    l1 = l0.title()
    return f"Result: {f1}  {l1}" #2 return format untuk memberikan nilai output dari perintah sebelumnya dan menjadi closing function terakhir walaupun sebelumnya masih ada fungsi yg sama

print(name_convert(input("What is your first name? "), input("What is your last name? "))) #command untuk memanggil hasil secara langsung