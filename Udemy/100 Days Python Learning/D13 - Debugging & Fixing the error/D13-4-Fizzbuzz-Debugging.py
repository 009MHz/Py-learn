for number in range(1, 101):
    print(f'Now checking number {number} ')
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])

"""
expected result: number/3 => fizz
expected result: number/5 => buzz
expected result: number/5 and 3 => fizzbuzz
expected result: printed number ga pake []
"""

"""
actual result
number/3 => print fizzbuzz and fizz
number/3 => still exist

number/5 => print fizzbuzz and buzz
"""

"""solutions
cek each number by print the current number after for loop code
print(f'Now checking number {number} ')
"""