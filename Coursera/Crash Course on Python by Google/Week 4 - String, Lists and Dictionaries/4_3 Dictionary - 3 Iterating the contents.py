"Example 1"
file = {'jpg': 10, 'txt': 21, 'py': 34, 'csv': 2}
# iterating the specific elements (keys only, or values only)
file.keys()  # dict_keys(['jpg', 'txt', 'py', 'csv'])
file.values()  # dict_values([10, 21, 34, 2])

# Case 1 iterating the keys
print("Case 1 iterating the keys, method 1")
for x in file:
    print(x)  # jpg, txt, py, csv
print("\nCase 1 iterating the keys, method 2")
for x in file.keys():
    print(x)

# Case 2 iterating the values
print("\nCase 2 iterating the values")
for x in file.values():
    print(x)

# Case 3 iterating the elements as a tuple
print("\nCase 3 iterating the elements as a tuple")
for type, amount in file.items():
    print(f"extension: {type}, number: {amount}")



"Example 2: letters count function"
print("\nExample 2: letters count function")
def count_letters(text):
    # initialize the holder (empty dictionary)
    result = {}
    # iterating the given parameter
    for letter in text:
        # adding the iterated text when it's not added to the holder
        if letter not in result:
            result[letter] = 0
        # adding the amount when the given letter is exist
        result[letter] += 1
    return result


print(count_letters("aaaaaaarghh"))  # {'a': 7, 'r': 1, 'g': 1, 'h': 2}
print(count_letters("Lorem Ipsum dot amet dolor"))
# {'L': 1, 'o': 4, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'I': 1, 'p': 1, 's': 1, 'u': 1, 'd': 2, 't': 2, 'a': 1, 'l': 1}


"""Real Situation concept
Analyzing logs in the server & counting the errors that occurs 
    1. Using the type of error as the key
    2. Increment the associated value each time the same error occurs
    3. Exporting the result as a log or simply printout the summary
"""
