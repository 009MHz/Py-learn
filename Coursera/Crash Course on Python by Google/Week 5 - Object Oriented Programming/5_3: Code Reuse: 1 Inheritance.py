"""In object-oriented programming, the concept of inheritance allows you to build relationships between objects,
grouping together similar concepts and reducing code duplication. Let's create a custom Fruit class with color and
flavor attributes: """
class Fruit:  # The Ancestor (Parent)
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):  # The children
    pass

class Grape(Fruit):
    pass

"""
- In python we user parentheses in the class declaration to show an inheritance
- It means the Grape & Apple will having same attributes like the Fruit (children)
- And the relation between Apple & Grape are siblings they may have same attributes but they will have different instances
    # apple instances -> color: red, flavor: sweet
    # grape instances -> color: purple, flavor: sweet
"""
"Example 1: Assigning same attributes on the children class"
print("\nExample 1: Assigning same attributes on the children class")
# Assigning instances to the siblings
fuji = Apple('green', 'juicy')  # assigning Fuji apple that has green color , and juicy flavor
carnelian = Grape('purple', 'sour')  # assigning carnelian grape that has purple color , and sour flavor
print(fuji)  # <__main__.Apple object at 0x100c2ffd0>
print(fuji.color)  # green
print(carnelian)  # <__main__.Grape object at 0x10262beb0>
print(carnelian.color)  # purple

"Example 2: Passing different instances on the children class"
print("\nExample 2: Passing different instances on the class")
class Animal:
    sound = ''

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.sound}, call me {self.name}")

class Cat(Animal):  # assigning Cat from Animal class that having sound like below
    sound = "meeowww"
print(Cat)  # <class '__main__.Cat'>
#print(Cat.sound())  # TypeError: 'str' object is not callable, sound is not a method
print(Cat.sound)  # meeowww

"To make it works (calling the name and sound), we need to assign the class into a variable then calling it"
tengil = Cat('Tengil')
tengil.sound  # meeowww
tengil.speak()  # calling the function to execute the print function -> meeowww, call me Tengil

class Dog(Animal):
    sound = 'wauufff'
asu = Dog('Kowe')
asu.speak()  # wauufff, call me Kowe

"""REMEMBER:
When assigning the Class under inheritance, we need to assign all attributes that defined on the ancestor"""

"Example 3: Clothing classes"
print("\nExample 3: Clothing classes")
class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()

"""REAL WORLD CONCEPT
- In the system of company, we may have a Class called employee
- On this employee, we might have the attributes such as:
    # full name
    # employee ID 
    # user group, etc
- This employee class could have some methods such as:
    # check the group they're belong (staff, managerial, supervisor, etc)
    # check the division (marketing, tech, support, HR, etc)
    # creating email address based on their full name
"""