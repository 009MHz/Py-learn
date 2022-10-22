"""Representing a concept in Python Code"""


class Apple:
    pass


# Writing a class will storing a keyword to a computer that we'll add a new class
# we follow this with the name and a colon
# on python the class name will always using a Titlecase
# After the colon, the class body will be indented to the right
# the pass function is represent a place holder that, the class will not do anything

"Example 1: Adding information to the created Class"


class Apple:
    color = ""
    flavor = ""


# We give 2 variable under the Apple class
# from now on Apple will having 2 attributes, which is 'color' & 'flavor'
# later on we'll use the attributes to give this Apple a content

"Example 2: passing the data for the attributes"
# Now we're creating new instance of the Apple class
# Assigning it into fuji variable that means Apple Fuji
fuji = Apple()
# After assign it, this apple will converted into a object (Apple Fuji) then we'll give the details
# about what Apple Fuji is, using the dot notation
fuji.color = 'red'
fuji.flavor = 'sweet'
print(fuji)  # <__main__.Apple object at 0x1008a7c10>
print(fuji.color)  # red
print(fuji.flavor)  # sweet

"""DOT NOTATION
Lets you access any of the abilities / function of the object might have (called methods)
or
information / value it might store (called attributes)
The attributes and methods of some objects can be other objects and can have attributes and
methods of their own
"""

"Example 3"
print("\nExample 3")
class Flower:
    color = 'unknown'


rose = Flower()
rose.color = 'red'

violet = Flower()
violet.color = 'blue'

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)
