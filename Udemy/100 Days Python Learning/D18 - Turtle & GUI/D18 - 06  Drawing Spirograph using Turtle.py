from turtle import Turtle, Screen
import random

leo = Turtle()
canvas = Screen()
canvas.colormode(255)
leo.pensize(1)
leo.speed(0)  # 0 : fastest, 1: slowest, 6 : normal, 10: fast


def colorize():
    """Applying random RGB value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(circle_gap):
    for x in range(int(360 / circle_gap)):
        leo.color(colorize())  # randomize the color
        leo.circle(100)  # spiro size (circle radius)
        leo.setheading((leo.heading() + circle_gap))  # nggeser circle drawing direction based on input degrees


spirograph(5)
canvas.exitonclick()