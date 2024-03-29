from turtle import Turtle, Screen
import random

leo = Turtle()
canvas = Screen()
canvas.colormode(255)  # fixing turtle not displayed using RGB color
directions = [0, 90, 180, 270]
distance = random.randint(30, 50)
leo.pensize(10)
leo.speed(9)  # 0 : fastest, 1: slowest, 6 : normal, 10: fast


def random_color():
    """Applying random RGB value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colorize = (r, g, b)
    return colorize


for x in range(150):
    leo.pencolor(random_color())
    leo.forward(distance)
    leo.setheading(random.choice(directions))

canvas.exitonclick()