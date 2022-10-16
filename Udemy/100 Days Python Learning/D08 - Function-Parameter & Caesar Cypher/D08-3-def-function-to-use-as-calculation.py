#Write your code below this line 👇
import math #code untuk menambah formula supaya semua deciamal selalu ROUNDUP
def paint_calc(height,width,cover):
    cans_number = test_h*test_w / cover
    cans = math.ceil(cans_number) #ROUNDUP angka desimal dari hasil yg didaapat
    print(cans_number)
    print(cans)
    print(f"You'll need {cans} of paint")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


