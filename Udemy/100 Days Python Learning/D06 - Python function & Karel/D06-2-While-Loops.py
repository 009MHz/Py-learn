#While Loops
#For loops digunakan untuk nge loop suatu list atau range data, contoh:
     # for item in list_of_items:
     #     do something to each item
    # for go in range(6):
    #     path()
#Sementara untuk while loops:
    #Melakukan sesuatu perintah secara menerus selama command yang diberikan "is true" 

# while something_is_true:
#     do_something_repeatedly
#While loops bisa jadi infinite loop kalau condition tidak bisa berhenti / false, contoh
# while 5>3:
#     execute()
#maka console akan menjalankan execute() sampai taun depan, karena 5 selalu lebih dari 3 dan tidak mungkin salah
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def path():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
executed_path = 6
while executed_path >0: #format: command(while) executed_path>0 (condition)
    path() #result jika [condition] terpenuhi -> repeat sampai [condition] tidak terpenuhi lagi
    executed_path -= 1
    print(executed_path)
#check this link
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
        