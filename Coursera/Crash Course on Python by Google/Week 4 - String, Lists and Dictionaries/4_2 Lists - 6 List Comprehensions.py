"""Example 1: Creating a list with multiples of 7 from 7  - 70"""
# Normal list method
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)  # output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# List comprehension
multiple = [x * 7 for x in range(1, 11)]
print(multiple)  # # output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
"""List Comprehension let us create new lists based on sequences or ranges, so we can use this technique
whenever we want to create a list based on a range 
"""

"Example 2: generate a list of the length of the given strings"
print("\nExample 2: generate a list of the length of the given strings")
languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C#']
length = [len(x) for x in languages]
print(length)  # [6, 4, 4, 2, 4, 2]

"Example 3: generate a list of the number that divisible by 3 between 0-100"
print("\nExample 3: generate a list of the number that divisible by 3 between 0-100")
div3 = [x for x in range(0, 101) if x % 3 == 0]
print(div3)

"Example 4: function returns a list of odd numbers between 1 and n, inclusively."
print("\nExample 4: function returns a list of odd numbers between 1 and n, inclusively.")
def odd_numbers(n):
    result = [x for x in range(1, n+1) if x % 2 == 1]
    return result


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []