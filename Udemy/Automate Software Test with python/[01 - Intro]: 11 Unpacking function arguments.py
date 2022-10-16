'example 1: giving multiple arguments using *'
def sample(*args):
    # *args digunakan untuk memberikan >1 argument pada function yg dibuat
    # return error ketika tidak menggunakan * karena python akan declare it as a single argument
    return args

print(sample(1, 2, 5))  #returning (1, 2, 5) without error karena *args menerima >1 parameter

'example 2: Proper functions to multiply the given parameter'
def multiply(*args):
    print(f"\nCalled args: {args}")
    result = 1
    for x in args:
        result *= x
    return f"Multiply function result: {result}"

print(multiply(2,5,4))

'Example 3: Breaking the parameter using *'
def add(x, y):
    return f"\nAdd function result {x + y}"

num_list = [12, 9]
print(add(*num_list))  # 21
print(add(num_list))  # TypeError: add() missing 1 required positional argument: 'y', karena list tidak di breaking

num_dict = {'x': 14, 'y': 4}
print(add(**num_dict))  # for dictionary perlu menggunakan ** karena harus membongkar key & value
print(add(*num_dict))  #TypeError: add() missing 1 required positional argument: 'y'
print(add(num_dict))  #TypeError: add() missing 1 required positional argument: 'y'

print(add(*101,99,90))
# TypeError: add() argument after * must be an iterable, not int
# karena * digunakan untuk parameter yg memerlukan iteration, dan integer tidak memerlukannya

def apply(*args, operator):
    if operator == '*':
        return f"\nApply result: {multiply(*args)}"
    elif operator == '+':
        return f"\nApply result: {sum(*args)}"
    else:
        return "No valid operator on the passed parameter"

print(apply(80,17,2, '-'))
# TypeError: apply() missing 1 required keyword-only argument: 'operator'
# karea *args akan mengambil semua parameter sebagai argument termasuk operator nya '-'

print(apply(13, 15, 20, operator='*'))
