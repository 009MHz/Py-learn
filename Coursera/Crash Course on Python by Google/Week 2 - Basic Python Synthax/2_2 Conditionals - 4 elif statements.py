"""The number_group function should return "Positive" if the number received is positive, "Negative" if it's
negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen? """

def number_group(number):
    if ___:
        return "Positive"
    elif ___:
        return ___
    else:
        ___


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative


"""More Complex Branching with elif Statements Building off of the if and else blocks, which allow us to branch our 
code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more 
complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a 
comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the 
right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as 
false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful 
things! 
"""