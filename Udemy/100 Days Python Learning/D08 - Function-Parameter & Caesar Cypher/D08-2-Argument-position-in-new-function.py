#Simple Function
# def greet():
#   print("Hello Angela")
#   print("How do you do Jack Bauer?")
#   print("Isn't the weather nice today?")
# greet()

#Function that allows for input
# def input_greet(name):# def "nama function" ("parameter")
#     print(f'Hi, there "{name}"')
#     print(f'I told ya "{name}",This is just lesson for days 8')
#     print(f'Once, again Have a nice day "{name}"')
# input_greet("Hazeya") 

######################################################
#Functions with multiple input
def mix_greet(name, location): #cukup menambahkan "," pada parameter yg diminta supaya ada >1 parameter fungsi yg diminta
    print(f'Holla "{name}"') #fungsi untuk memanggil parameter pertama => "name"
    print(f"You are in '{location}' right?\n") #fungsi untuk memanggil parameter kedua => "location"

#Calling greet_with() with Positional Arguments
mix_greet("Hazeya","Yogyakarta")
#jika kedua argument di atas dibalik, maka "name" yang terpanggil akan menggunakan argument pertama[name = Yogyakarta] karena python sudah men-define argument 1 = "name", argument 2 = "location", be sure & recheck urutannya jika menggunakan pattern di atas
mix_greet("Yogyakarta","Hazeya")

#Calling function with Keyword Arguments
mix_greet(location="Yogyakarta", name = "Hazeya") #metode ini merupakan metode paling aman namun lebih panjang karena kita harus men-define argumen yang diminta, tapi mengurangi miss karena kita bisa menaruh urutannya dimanapun yg kita suka
