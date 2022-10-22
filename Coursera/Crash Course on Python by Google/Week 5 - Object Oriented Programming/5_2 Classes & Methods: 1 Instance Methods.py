"""RECAP"""
"""
Methods: Function that operate on the attributes of a specific instance of a class

"""

"Example 1:"


# creating the class
class Pig:
    # creating a function inside the class (methods)
    # in this case, we make the Pig creating a sound
    def speak(self):
        # this function is receiving a parameter called 'self'
        # this parameter represents the instance that the methods is being executed on
        # This will allow you to access attributes of the instance using dot notation
        print("oik oik")


hamlet = Pig()
# calling the methods from the classes
hamlet.speak()

"Example 2:"
print("\nExample 2")


class Piglet:
    # assign a attributes inside the class, that changeable later on
    name = "piglet"

    def speak(self):
        print(f"Oink oink, my name is {self.name}")
        # self.name means accessing the attributes name from the current instance
        # without using self.name this code will generate an error
        # NameError: name 'name' is not defined


babi = Piglet()  # Oink oink, my name is piglet
babi.speak()

"Case 1: Updating the name as an instance"
babi.name = 'Eluu'
# since we just change the attributes outside the function, we don't need () at the end of the processes
babi.speak()  # Oink oink, my name is Eluu

"Case 2: Creating new instance using same Class"
print("\nCase 2: Creating new instance using same Class")
celeng = Piglet()
# assigning new variable but using same class
celeng.name = 'Wildboar'
celeng.speak()  # Oink oink, my name is Wildboar

"""SUMMARIES
Variables that have different values for different instances of the same class are called instance variables
just like the example from case 2
"""

"Example 3: Method to returning any values after receiving parameter update"
print("\nExample 3: Method to returning any values after receiving parameter update")
class Doggy:
    years = 0

    def dog_years(self):
        return self.years * 18


kiku = Doggy()  # assign the class to variable
print(kiku.dog_years())  # 0
kiku.years = 1.5  # updating the attributes
print(kiku.dog_years())  # calling the methods after update -> 27
