"""for loop: Iterates over a sequence of values"""
for x in range(5):
    print(x)  # return the number from 0-5 except 5

"""IMPORTANT
    1. In Python, and a lot of other programming languages, a range if numbers will start with
    the value 0 by default
    2. The list of numbers generated will be -1 from given value 
"""

# example 1:
"""Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 
and x (not included). Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (
not included). """
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(0, x):
        sum += square(n)
    return sum


print(sum_squares(10))  # Should be 285

# example 3:
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for x in friends:
    print("Hi " + x)


"""SUMMARIES
    - Use for loops when there's a sequence of elements that you want to iterate
    - Use while loops when you want to repeat an action until a condition changes
"""