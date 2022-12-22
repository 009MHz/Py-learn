import pandas
import turtle

"""1. Background map"""
# 1.1 Define the background
screen = turtle.Screen()
screen.title("U.S. States Guess Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# 1.2 Define the location guessing position to show the input position:
# https://cutt.ly/90KesIL

"""3. Game Continuation"""
# 3.1 Define the game condition for looping
correct_answer = []
while len(correct_answer) != 50:

    # 1.3 Define the prompt for user input
    loc_prompt = screen.textinput(title=f"{len(correct_answer)}/50 Answers", prompt="Guess the States").title()
    print(loc_prompt)

    """2. Check the input vs correct data"""
    # 2.1 read the CSV & convert to python data
    data = pandas.read_csv("50_states.csv")
    states = data.state.to_list()

    # 2.2 Validate the correct answer
    if loc_prompt in states:  # Showing the result on the map
        correct_answer.append(loc_prompt)
        print(correct_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct = data[data.state == loc_prompt]
        t.goto(int(correct.x), int(correct.y))
        # t.write(correct.state)  # will be writing CSV pandas reading
        t.color('blue')
        t.write(correct.state.item())

    # 2.3 Providing endpoint to exit the game
    elif loc_prompt == "Exit":

        # 3.2 Exporting remaining answer to csv files
        missing_states = []
        for x in states:
            if x not in correct_answer:
                missing_states.append(x)
        logs = pandas.DataFrame(missing_states)
        print(logs)
        #logs.to_csv("key_answers.csv")
        break

