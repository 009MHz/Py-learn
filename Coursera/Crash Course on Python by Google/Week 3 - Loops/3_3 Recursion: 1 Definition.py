Recursion = "The repeated application of the same procedure to a smaller problem"
"real concept: Russian Doll toy"
"""
- Recursion lets us tackle complex problems by reducing the problem to a simpler one
- In programming, recursion is a way of doing a repetitive task by having a function call itself
- A recursive function calls itself usually with a modified parameter until it reaches specific condition
- This specific condition is usually called the 'base case'
"""
# by taking the real concept, the base case condition is the smallest doll inside the Russian Doll

"Example 1"
def factorial(x):
    print(f"Factorial called with {x}")
    if x < 2:  # defining the base case where x is smaller than 2
        print("Returning 1")
        return 1  # will return 1 when the x value is smaller than 2
    result = x * factorial(x-1)  # recursive case to call the function -1 within the function
    print(f"Returning {result} for factorial of {x}")
    return result


factorial(4)

"Example 2"
print("\nExample 2")
"""The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 
1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps 
to make this work: """
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15