from turtle import Turtle, Screen
from turtle_colors import colors
import random

don = Turtle()
canvas = Screen()

"""Creating Dashed LIne"""
# for x in range(10):
#     don.forward(5)  # move the turtle
#     don.penup()  # creating blank trail
#     don.forward(5)  # move again
#     don.pendown()  # creating black trail

"""Creating square - decagon shape"""
def shapes(sides_number):  # function dengan jumlah sisi pada argumennya
    for x in range(sides_number):
        angle = 360 / sides_number  # assigning variable untuk menentukan sudut belok turtle
        don.forward(50)
        don.right(angle)  # controlling the turtle turn angle

# drawing the shapes
for i in range(3,11):  # looping control dari 3 sisi (triangle) - 11 (decagon)
    shapes(i)
    # adding random color on the line
    don.color(random.choice(colors))