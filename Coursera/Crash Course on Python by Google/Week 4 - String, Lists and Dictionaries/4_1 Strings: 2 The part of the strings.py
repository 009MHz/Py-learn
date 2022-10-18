"""String indexing: operations that lets us access the character in a given position or index using square brackets
and the number of the position we want """
name = 'Jedai'
print(name[0])  # python indexing is start from 0 instead 1 => J
print(name[1])  # e
# print(name[7])  # Accessing an index that out of range will resulted as an error
# IndexError: string index out of range

"""Using negative index allow us to reach the end of the string without concerning the length of the strings"""
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print(text[-1])  # Taking the last text position -> 't'
print(text[-2])  # Taking the last text position -1 => 'i'

# example 1
print('\nexample 1')
"""Modify the first_and_last function so that it returns True if the first letter of the string is the same as the 
last letter of the string, False if they’re different. Remember that you can access characters using message[0] or 
message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing. """
def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

"""Slicing: a method to take the portion of a string that contain more than one character, sometimes called a substring
We do that by creating a range using a colon as a separator 
"""
#example 2: Slicing
print("\nexample 2: Slicing")
color = "Magenta"
print(color[2:5])   # Taking the third character up to fifth character -> gen
print(color[3:])    # Taking the fourth character till the end of text -> enta
print(color[:4])    # Taking the first character up to fourth character -> Mage

