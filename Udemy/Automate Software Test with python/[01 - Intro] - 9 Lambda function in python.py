# Todo: Definitions:"""
#  Lambda function used for returning the value and specially operate on inputs and return output
#  This functions never be used to perform actions"""

'example 1'
def add(x, y):
    return x + y

print(add(5, 7))  # 12

'we can shorten mentioned function with lambda function like this'
lambda x, y: x + y
(lambda x, y: x + y)(5, 7)
print((lambda x, y: x + y)(5, 7))

"""Lambda Rules:
1. Format: lambda parameter list (x,y) : return value from the function (x+y)
2. don't assign variable / name in lambda function to avoid confusion since lambda is short function and we don't often
using it with a name
3. when the lambda doesn't have a name it will not executed unless we define the function on the same line with it
4. the workaround from rule no.3 is using the proper format: (line 12)
( lambda {parameter list}: {return value from the function (x+y)} (argument that will be executed within the lambda)
5. last one, we need surround it with the command that will be used (e.g: print) with correct format (line 13)
"""

"Example 2: doubling the value inside the list"
print("\nExample 2: doubling the value inside the list")


# 1 define the functions
def double(x):
    return x * 2


animals = ['rat', 'bat', 'cat', 'mad']
# 2a. calling the functions within the list comprehension
doubled = [double(x) for x in animals]
print(doubled)  # ['ratrat', 'batbat', 'catcat', 'madmad']

# 2b. using 'map' function
# format: map(called functions, passed values)
# will executing the function given to reproduce the passed values
# passed values can be a sequence (list, set , tuples)
doubled = map(double, animals)
print(doubled)  # will be returned as map object -> <map object at 0x10504cb80>
print(list(doubled))  # returned as correct list ['ratrat', 'batbat', 'catcat', 'madmad']

"Example 3: doubling the value inside the list using the lambda concept"
print("\nExample 3: doubling the value inside the list using the lambda concept")
hero = ["Lin", "Wan", "Tan", "Sun"]
doubled_name = [(lambda x: x * 2)(x) for x in hero]  # ['LinLin', 'WanWan', 'TanTan', 'SunSun']
"""Cara kerja:  lambda menduplikat value x yang di looping dari list nya hero"""

map_name = list(map(lambda x: x * 2, hero))  # ['LinLin', 'WanWan', 'TanTan', 'SunSun']
"""cara kerja: 
1. value yg ada di list hero akan di iterate oleh map
2. iteration dari map akan dicap sebagai x oleh lanbda
3. kemudian x akan diduplicate oleh lambda "x: x * 2"
4. yang terakhir list akan menyusun hasil duplikasi and returned as a new list
"""


# Example 1: normal
def perkalian(x, y):
    print("Example 1: Normal")
    print(x * y)


perkalian(8, 5)  # 40

# Example 2: assigning the function result into variable without return
def reduce(x, y):
    print(x - y)


print("\nExample 2: assigning the function result into variable without return")
result = reduce(8, 5)
print(f"Line in seharusnya mengahsilkan 3, tapi ini hasilnya '{result}'")  # None
print(reduce(6, 2))  # 4 & None
'''Kenapa hasilnya None?
    1. Karena hasil yang berupa printing output sudah diambil pada [eromtah sebelumnya]
when called to print in the same time
    2. Akibatnya variable yg diassign tidak akan menghasilkan output apa-apa (None)
'''


# Example 3: Workaround using return
def divider(x, y):
    return x / y


print("\nExample 3: Workaround using return")
divider(91, 3)  # Tidak menghasilkan apa-apa karena output nya berupa value, bukan berupa string
result = divider(34, 5)  # # Tidak menghasilkan apa-apa karena output nya berupa value, bukan string
print(result)  # Ini baruuu bisa -> 6.8
print(divider(22, 7))  # 3.142857142857143
