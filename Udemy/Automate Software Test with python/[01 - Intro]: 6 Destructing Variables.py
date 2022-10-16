source = "https://blog.teclado.com/destructuring-in-python/"
'''Definition'''
"""Destructuring (also called unpacking) is where we take a collection, like a list or a tuple, and we break it up 
into individual values. This is quite useful, as it enables us to do things like destructuring assignments, 
where we assign values to several variables at once from a single collection. """

x = (10, 14)
#For a tuple kita boleh menghilangkan kurung nya dan tidak akan dianggap sebagai violation
y = 8, 16
print(y)  # (8, 16)

'example 1, assigning more than 1 value without kurung'
priest = 'support', 'heal'  # define the variable and the values
role, task = priest  # assigning the values into 2 variables
print(role, task)  # support heal

'example 2:'
print("\nconverting the given data into tuple")
raid_ATK = {'Moonlord': 320, 'Raven': 480, 'Saint': 200, 'Sniper': 400}
print(raid_ATK.items())  # still return "dict_items)
# dict_items([('Moonlord', 320), ('Raven', 480), ('Saint', 200), ('Sniper', 400)])
print(list(raid_ATK.items()))  # adding list, will remove the "dict_items"
# [('Moonlord', 320), ('Raven', 480), ('Saint', 200), ('Sniper', 400)]

'destructing the tuples'
print("\n destructing the tuples")
for des in raid_ATK.items():
    print(des)

'example 3'
print("\nDestructing the list value of tuple")
party = [('Paladin', 63, 'Tanker'), ('Sniper', 54, 'DPS'), ('Accolyte', 56, 'Healer'), ('Sage', 71, 'Support')]
for char, level, role in party:
    print(f"Class name: {char}, Level: {level}, role: {role}")
    # Class name: Paladin, Level: 63, role: Tanker

print("\nAnother method to unpack")  # returning same result with script above
for x in party:
    print(f"Class name: {x[0]}, Level: {x[1]}, role: {x[2]}")


# for name, level in party:
#     print(f"Class name: {name}, Level: {level}")
    # ValueError: too many values to unpack (expected 2)
    # there are 3 values in the tuples but only 2 given to extract

print('\nIgnoring the list to avoid unpack error')
"""menggunakan underscore pada variable dalam iterating value from tuple, akan mengabaikan value yg ada """
hero = ('Crusader', 76, "Tanker")
name, _, role = hero  # taking the name, role, and ignoring the level value from hero variable
print(f"Class: {name}, role: {role}")  #Class: Crusader, role: Tanker

print('\nCollecting the value from the list and breaking into 2 lists')
head, *follower =['satu', 2, 'tiga', 'empat', 5]  # head = satu & *follower = [2, 'tiga', 'empat', 5]
*head, follower =['satu', 2, 'tiga', 'empat', 5]  # *head = ['satu', 2, 'tiga', 'empat'] &  follower = 5




