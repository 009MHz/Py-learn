# Class type selalu diawali dengan huruf kapital
# import turtle
# raph = turtle.Turtle()
# asssigning the turtle class into variable

'second method'
turtle_docs = "https://docs.python.org/3/library/turtle.html"
turtle_color = "https://cs111.wellesley.edu/reference/colors"
from turtle import Turtle, Screen  # from "module" importing the Class

leo = Turtle()
#print(leo)  # <turtle.Turtle object at 0x100e48e20>
leo.shape('turtle')
leo.color('coral')
leo.forward(100)

monitor = Screen()  # assigning the module Class into variable
print(monitor.canvheight)  # printing the object inside the Screen Class, dalm hal ini function canvheight
monitor.bgcolor("azure")
monitor.exitonclick()

