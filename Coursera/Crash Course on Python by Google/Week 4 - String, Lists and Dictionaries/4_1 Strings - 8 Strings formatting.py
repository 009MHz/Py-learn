# example 1: passing the int & str into text without converting
print("Example 1: passing the int & str into text without converting same types")
name = 'Lenna'
number = len(name) * 3
"method 1: using empty curly brackets"
print("Hi {}, your lucky number is {}".format(name, number))
"method 2: passing the expressions inside the curly brackets"
print("your lucky number is {number}, {name}".format(name=name, number=number))
"method 3: using f string"
print(f"Hi {name}, your lucky number is {number}")

# example 2
print('\nexample 2')
def student_grade(name, grade):
    return f"{name} received {grade}% on the exam"


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# example 3: format to round the decimal inside the strings
print('\nExample 3: format to round the decimal inside the strings')
price = 7.5
total = price * 1.09
print(price, total)     # 7.5 8.175
print("Base Price: ${:.2f}. With tax: ${:.2f}".format(price, total))   # Base Price: $7.50. With tax: $8.18
'second method'
print(f"Base price: ${price:.2f}. With tax: ${total:.2f}")
# .2f is used to round the decimal number inside the string format without changing the variable before passed here

# example 4: reformatting the temperature conversion using .2f
print("\nExample 4: reformatting the temperature conversion using .2f")
def to_celsius(x):
    return (x-32)*5/9


for x in range(0,101,10):
    print(f"{x:3} F | {to_celsius(x):6.2f} C")
    # x:3 is format to add 3 spaces (including the x) to adjust the alignment
    # matched the alignment between 1 & 2 digit with 3 digits
    # before: "0 F |", after: "  0 F |"
    # x:6.2f is format to add 6 spaces and rounding the decimals into 2 format
    # before formatting: "| 21.11111111111111 C", after formatting: "|  21.11 C"