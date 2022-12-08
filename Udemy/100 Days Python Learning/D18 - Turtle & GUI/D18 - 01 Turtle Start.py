# Turtle docs: https://docs.python.org/3/library/turtle.html
# Turtle color: https://cs111.wellesley.edu/reference/colors
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
leo = Turtle()
leo.shape("turtle")
leo.color("red4")



# Drawing a square
for x in range(4):
    leo.right(90)
    leo.forward(100)



screen.exitonclick()