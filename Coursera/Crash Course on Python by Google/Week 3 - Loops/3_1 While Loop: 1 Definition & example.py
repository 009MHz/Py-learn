"""Definition:
While loops Instruct our computer to continuously execute our code based on th value of a condition"""

'example: How many times will "Not there yet" be printed?'
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


"""Anatomy of while Loops 
A while loop will continuously execute code depending on the value of a condition. It 
begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code 
block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed 
if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep 
executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the 
next line of code will be executed. """

"example 2: Try passing different parameters to the attempts function to see what it does. "
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(3)


"""Example 3: In this code, there's an initialization problem that's causing our function to behave incorrectly. 
Can you find the problem and fix it?"""
def count_down(start_number):
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")


count_down(3)


"""Common Pitfalls With Variable Initialization You'll want to watch out for a common mistake: forgetting to 
initialize variables. If you try to use a variable without first initializing it, you'll run into a NameError. This 
is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. The fix is 
pretty simple: initialize the variable by assigning the variable a value before you use it. 

Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables 
with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first 
setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to 
initialize your variables before using them! 
"""