from turtle import Turtle, Screen
import random as r
from turtle_colors import colors

leo = Turtle()
canvas = Screen()
directions = [0, 90, 180, 270]
distance = r.randint(30, 50)
leo.pensize(10)
leo.speed(1)  # 0 : fastest, 10 : slowest

for x in range(150):
    leo.color(r.choice(colors))
    leo.forward(distance)
    leo.setheading(r.choice(directions))