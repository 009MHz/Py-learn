"""In math, the factorial of a number is defined as the product of an integer and all the integers below it. For
example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return
the right number. """
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120

"""example 1: Temperatur Converter"""
print("example 1: Temperatur Converter")
def to_celsius(x):
    return (x-32)*5/9


for x in range(0,101,10):  # looping the number 0 - 101 dengan kelipatan 10
    print(x, to_celsius(x))