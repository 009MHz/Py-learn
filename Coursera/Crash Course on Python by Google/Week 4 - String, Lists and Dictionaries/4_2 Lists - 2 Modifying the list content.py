"""Since Lists data type is mutable, we can update, add or remove the values inside list directly"""
'example 1'
print("adding value into the list")
weapon = ['sword', 'bow', 'staff']
weapon.append('dagger')  # adding new value on the last position from the order
print(weapon)  # output: ['sword', 'bow', 'staff', 'dagger']

weapon.insert(1, 'dual sword')  # adding new value on the given index
print(weapon)  # output: ['sword', 'dual sword', 'bow', 'staff', 'dagger']

weapon.insert(30, 'mace')  # adding new value on the position  yg melebihi kapasitas list
print(weapon)  # ['sword', 'dual sword', 'bow', 'staff', 'dagger', 'mace']

print("\nremoving value from the list")
weapon.remove('mace')
print(weapon)  # ['sword', 'dual sword', 'bow', 'staff', 'dagger']
# weapon.remove('violin')  # ValueError: list.remove(x): x not in list, karena given value tidak ada di list
weapon.pop(1)  # pop is used to remove the value from given index position which is 'dual sword'
print(weapon)  # ['sword', 'bow', 'staff', 'dagger']

print("\nudpating value from the list")
weapon[2] = 'wand'  # changing the value from index 2 (staff) to wand
print(weapon)

"""Real World situation concept:
Lists data type can be used to store information from hosts from a network
    1. Storing the data about online user -> adding into online list
    2. Removing the data about offline user -> removing from online list
"""

"Example 2"
print("\nExample 2")
"""The skip_elements function returns a list containing every other element from an input list, starting with the 
first element. Complete this function to do that, using the for loop to iterate through the input list """
def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for x in elements:
        # Does this element belong in the resulting list?
        if x != '':
            # Add this element to the resulting list
            new_list.append(x)
        # Increment i
        i += 1

    return new_list[::2]


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []
