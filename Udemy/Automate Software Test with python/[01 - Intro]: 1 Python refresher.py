# List, Tuples & Sets
list_weapon = ['Sabre', 'Dagger', 'Bow', 'Mace', 'Wand']  # keeping the order from its value
tuple_weapon = ('Sabre', 'Dagger', 'Bow', 'Mace', 'Wand')  # keeping the order from its value
set_weapon = {'Sabre', 'Dagger', 'Bow', 'Mace', 'Wand'}  # the order will keep changin on each execution

print(f"""
This is the result of list: {list_weapon}
This is the result of tuples: {tuple_weapon}
This is  the result of set: {set_weapon}""")

    # index slicing
list_weapon[3]  # mace
tuple_weapon[2]  # bow
set_weapon[0]  # not allowed for slicing since the value inside set always changed

    # modifying the values
list_weapon.append('Knuckles')  # ['Sabre', 'Dagger', 'Bow', 'Mace', 'Wand', 'Knuckles]
tuple_weapon.append('Knuckles')  # AttributeError: 'tuple' object has no attribute 'append'
set_weapon.add('Knuckles')  # adding 'Knuckles' to the set at random position
set_weapon.add('Knuckles')  
# not allowing duplication
# {'Mace', 'Wand', 'Dagger', 'Knuckles', 'Sabre', 'Bow'}

list_weapon.remove('Bow')  # ['Sabre', 'Dagger', 'Mace', 'Wand', 'Knuckles']
set_weapon.remove('Dagger')  # {'Mace', 'Bow', 'Knuckles', 'Sabre', 'Wand'}

