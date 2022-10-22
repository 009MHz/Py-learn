"""DEFINITION
- Constructor: a special method that we use to define multiple argument inside the class function
- Special Method: a function that starts & ends with double underscore (e.g: __init__)
"""
"Example 1"
class Apple:
    # the constructor is called when we call the Class' name
    def __init__(self, color, flavor):
        # constructor __init__ allows us passing 2 arguments on the function with above format
        # self: allow you to access attributes of the instance using dot notation
        # color & flavor: argument yg akan digunakan untuk mendefinisikan fungsinya
        self.color = color
        self.flavor = flavor


# Assigning instance variables on the Constructor
malang = Apple("red", "juicy")  # instant variables = Class("first argument", "second argument")
# when using constructor, we can pass directly the instant attributes after the class is called
# "red" will be assigned to color since the __init__ first argument is color
# 'juicy' will be assigned to color since the __init__ second argument is flavor

print(malang.color)  # red
print(malang.flavor)  # juicy

"Example 2"
print('\nExample 2')
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f'hi, my name is {self.name}'


# Create a new instance with a name of your choice
me = Person('Hazeya')
# Call the greeting method
print(me.greeting())

"Example 3: What will happen when we don't specify the object of the class"
print("\nExample 3: What will happen when we don't specify the object of the class")
print(malang)  # <__main__.Apple object at 0x1026d3fd0>
# python will be using a default method that prints the position stored in the computer's memory
# workaround: using STR special methods to return it as proper text
class Mango:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return f"This mango has {self.color} & {self.flavor} flavor"
        # must be using self.color meskipun diatas sudah didefinisikan
        # karena return ini mengambil variable dari methods lain meskipun dalam kelas yg sama

manalagi = Mango("orange", 'sour')
print(manalagi)
# This mango has orange & sour flavor
# tanpa menggunakan __str__ line diatas akan memberikan output: <__main__.Mango object at 0x1012e3c70>
print(manalagi.flavor)  # sour
print(manalagi.color)  # orange