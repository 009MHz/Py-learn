# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet(): #normal function tanpa permintaan adanya kondisi tambahan
#     print("Hi there")
#     print("This is just lesson for days 8")
#     print("So yeah, I need 3 statements for that")
# greet()
#def greet(susah): adalah fungsi dengan tambahan input / situasi dalam "susah"
def input_greet(name):# def "nama function" ("parameter")
    print(f'Hi, there "{name}"')
    print(f'I told ya "{name}",This is just lesson for days 8')
    print(f'Once, again Have a nice day "{name}"')
input_greet("Me") # "nama function" ("argumen")
#argumen merupakan suatu field yg harus diisi supaya semua perintah dalam function bisa di-run, karena pada line 11 kita sudah mengatur nya pada parameter yang ditetapkan sebelum mendefinisikan fungsi baru nya (line 12 - 15) yang mengambil data dari {name} atau parameter yang kita setup
