"""When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element
in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a
list, along with the index of the element in question? You can do this using the enumerate() function.
The enumerate() function takes a list as a parameter and returns a tuple for each element in the list.
The first value of the tuple is the index and the second value is the element itself. """

"Example 1: normal iterating elements"
print("Example 1: normal iterating elements")
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for x in animals:
    print(x)
    chars += len(animals)
print(f"Total chars: {chars} total unit: {len(animals)}")

"Example 2: Enumerates to iterating elements and return it as tuple"
print("\nExample 2: Enumerates to iterating elements and return it as tuple")
winners = ['Real Madrid', 'Barcelona', 'AC Milan', 'Bayern Munich']
for x in enumerate(winners):
    print(x)  # (0, 'Real Madrid')

"Example 2-1: Unpack it to 2 variable"
for index, club in enumerate(winners):
    print(f"No.{index} {club}")  # No.3 Bayern Munich

"Example 2-2: not working"
# for index, club in winners:  # ValueError: too many values to unpack (expected 2)
#     print(f"No.{index} {club}")

"Example 3: Creating a lists that holds person name and email adress"
print("\nExample 3: Creating a lists that holds person name and email address")
'expected result: John Doe <john@email.com>'

# Todo 1: creating a function that receive the name parameter
def full_emails(people):  # people is a tuple that holds name & email address
    # Todo 2: creating a variable from the function result
    result = []
    # Todo 3: Unpacking the given tuple
    for email, name in people:
        # Todo 4: adding the unpacked element into the result
        result.append(f"{name}, <{email}>")
    return result


print(full_emails(
    [
        ("john.doe@email.com", "John Doe"),
        ("lorem@email.com", "Lorem Ipsum"),
        ("bruce@wayne.com", 'Bruce Wayne')
    ]
))

"Example 4"
print("\nExample 4")
"""he skip_elements function to return every other element from the list, this time using the enumerate function to 
check if an element is in an even position or an odd position. """
def skip_elements(elements):
    # code goes here
    new_list = []
    new_index = 0
    for index, content in enumerate(elements):
        if index %2 == 0:
            new_index += index
            new_list.append(content)
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']