base = [1, 5, 3, 7, 9]
doubled = []

'''Example 1'''
# Common method
for x in base:
    doubled.append(x * 2)

    # comprehensions
doubled = [x * 2 for x in base]

'''Example 2'''
weapon = ['long sword', 'dual sword', 'scimitar', 'bastard sword', 'katana', 'staff']
sword = []
# common method
# for z in weapon:
#     if z.endswith('sword'):
#         sword.append(z)
# print(sword)

# comprehension
sword = [z for z in weapon if z.endswith('sword')]
print(sword)
