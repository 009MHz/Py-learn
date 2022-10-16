#While loops with IF function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def manouver():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        manouver()
    else:
        move()
#cara penggunaan:
#while [condition]:
    #if (condition):
        #eksekusi dari condition
    #elif / else (condition):
        #eksekusi dari conhdition
#maka console akan ngeloop comand while tersebut dengan tambahan syarat yang ditentukan dari IF child nya