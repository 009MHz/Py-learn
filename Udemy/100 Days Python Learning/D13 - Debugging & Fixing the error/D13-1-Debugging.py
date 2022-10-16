############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# """20 is out of range, ganti range nya (1,21)"""

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# """random 6 is out of function, ganti range di randint menjadi (0,5)"""

# Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# """
# <1980 no valid response
# =1980 no valid response 
# =1994 no valid response, fixing it by ad >= 1994 or <=1994 di if statement nya """


# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# """
# 1. print statement is not indented => majuin 1 indent
# 2.age nya masih di format string, dan if statement tidak berfungsi untuk execute string > integer => ganti code di age menjadi int(input("How old are you?"))
# 3. print ga pake f' formatting dan {age} tidak akan terconvert ke input user """

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# """
# 1. gunakan print untuk mencari tau hasil tiap variable
# 2. identify value yg tidak sesuai
# 3. observe the code (words..== int...)
# 4. ganti code nya, run ulang (words..=int...)
# 5. hapus print code nya dan rapikan lagi code block nya """

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
"""
1. expected result: [2, 4, 6, 10, 16, 26]
2. actual result [26]
3. use debugger, detected issue: result hanya ngambil last calculation [13*2]
4. solutions => majuin 1 indent di function append nya
"""