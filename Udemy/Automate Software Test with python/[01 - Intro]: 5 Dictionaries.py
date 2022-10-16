char_weapon = [
    {"role": "Barbarian", "main": 'greatsword', 'side': 'bangle'},
    {"role": "Sniper", "main": 'bow', 'side': 'arrow'},
]
#getting the value inside the dictionary
print(char_weapon[0]['role'])  #Barbarian

raid_ATK = {'Moonlord': 320, 'Raven': 480, 'Saint': 200, 'Sniper': 400}
#returning the key and value at the same time
'''first method'''
for x in raid_ATK:
    print(f"{x} ATK score is {raid_ATK[x]}")

'''second method'''
print("\nSecond method result ")
for role, attack in raid_ATK.items():
    # search thoroughly the role and attack variable (temporary) inside the
    # dict_items([('Moonlord', 320), ('Raven', 480), ('Saint', 200), ('Sniper', 400)])
    print(f"Role: {role}, total atk: {attack}")

"""Summary"""
dict.items() : returning the dictionary key and values as a set
dict.values() : returning the dictionary values only
dict.keys()  : returning the dictionary keys only

