import random
import turtle as t
from color_extraction import color_list

# 1: Assigning turtle mode
t.colormode(255)  # setup for canvas to approve multi color
canvas = t.Screen()  # assign the screen variable
leo = t.Turtle()  # assign the turtle variable
leo.speed(8)

# 4: Removing the turtle and the drawn line
def debug(switch):
    if switch == "off":
        line = leo.penup()
        header = leo.hideturtle()
        return True
    elif switch == "on":
        return False


debug("on")

# 2: setup the line pattern
leo.setheading(225)
leo.forward(350)
leo.setheading(0)
dots = 100

for x in range(1, dots + 1):  # dot amount (repetition)
    """drawing one dot lines"""
    leo.dot(20, random.choice(color_list))  # assigning turtle dot size, and dot color
    leo.forward(50)  # space distance

    # 3: setup turtle movement pattern
    if x % 10 == 0:  # condition to move to the next line position after 1 line (10 dots) have been drawn
        """Changing the direction"""
        leo.setheading(90)
        leo.forward(50)
        leo.setheading(180)

        """Return to the first dote column position"""
        leo.forward(500)  # space distance x space repetition

        """Change the direction to draw the next line"""
        leo.setheading(0)

canvas.exitonclick()