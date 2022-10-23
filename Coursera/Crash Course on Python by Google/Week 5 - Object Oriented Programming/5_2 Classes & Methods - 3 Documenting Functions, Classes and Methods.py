"""Classes can be not so beginner friendly. In that case we can also using help() function to check what will happen
under our own created Classes"""
"Example 1"
print("Example 1")


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return f"This apple has {self.color} & {self.flavor} flavor"


help(Apple)  # command to get the documentation related to our Apple classes
"""Help on class Apple in module __main__:

class Apple(builtins.object)
 |  Apple(color, flavor)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, color, flavor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)"""

"Example 2: Using docstring or comment to write the documentation about our code"
print("\nExample 2: Using docstring or comment to write the documentation about our code")


def to_seconds(hours, minutes, seconds):
    """return the amount of seconds from passed argument"""
    return hours * 3600 + minutes * 60 + seconds


help(to_seconds)
"""Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    return the amount of seconds from passed argument"""

"Example 3: Adding documentation about class Person"
print("\nExample 3: Adding documentation about class Person")
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        """Outputs a message with the name of the person"""
        print("Hello! My name is {name}.".format(name=self.name))


help(Person)

