'Example 1: obtaining the users name as a key and return all the data as a value'
users = [
    (118910, 'Paladin', 'Lilia', 63),
    (119181, 'Sniper', "Azura", 54),
    (117182, 'Accolyte', 'Kitana', 56),
    (187193, 'Sage', 'Mazia', 71)
]  # user id, user character, username, character level

#1a. normal method
print("Executing the scenario with the normal method")
scene1a = {}
for x in users:
    scene1a[x[2]] = x
print(scene1a)  # {'Lilia': (0, 'Paladin', 'Lilia', 63),...}

#1b. normal method
print("\nExecuting the scenario with the dictionary comprehension")
scene1b = {stat[2]: stat for stat in users}
# concept:
    # looping the value in users list as stat
    # returning the value[2] form stat (118910, 'Paladin', 'Lilia', 63) as the key
    # assigning all contents in each tuples as a value from the key

print(scene1b)  # {'Lilia': (0, 'Paladin', 'Lilia', 63),...}

