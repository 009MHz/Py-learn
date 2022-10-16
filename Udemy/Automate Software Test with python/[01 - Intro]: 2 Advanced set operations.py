weapons = {'Sabre', 'Dagger', 'Bow', 'Mace', 'Staff'} 
ranged = {'Bow', 'Staff'} 

    # separating the unchoosen elements by check the duplication
melee = weapons.difference(ranged)
# melee = check the difference elements inside ranged that belongs to weapons
print(melee)  # {'Sabre', 'Dagger', 'Mace'}

    # joining different elements into same sets withou value duplication
priest = {'staff', 'wand', 'robe','cloak' }
wiz = {'staff', 'orbs', 'grimoire', 'robe'}
equipment = priest.union(wiz)
# joining all elements from wiz & priest into equipment variable
print(equipment)  # {'orbs', 'robe', 'wand', 'staff', 'grimoire', 'cloak'}

    # validating the duplication elements that merged into one
priest = {'staff', 'wand', 'robe','cloak' }
wiz = {'staff', 'orbs', 'grimoire', 'robe'}
similar = priest.intersection(wiz)
print(similar)  # {'staff', 'robe'}