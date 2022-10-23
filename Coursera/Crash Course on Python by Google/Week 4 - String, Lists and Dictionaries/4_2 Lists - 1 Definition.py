"""
- Data types that contain a multiple values
- The values are separated by commas
- Using square brackets [] to define this data types
"""
x = ['this', 'is', 'the', 'data', 'type', 'that', 'called', 'lists']
type(x)  # -> <class 'list'>
print(x)  # -> ['this', 'is', 'the', 'data', 'type', 'that', 'called', 'lists']
len(x)  # -> 8
'is' in x  # -> True
'hello' in x  # -> False
print(x[0])  # this
print(x[-1])  # lists
print(x[1:4])  # ['is', 'the', 'data']
print(x[1:4:2])  # ['is', 'data']
print(x[:4])  # ['this', 'is', 'the', 'data']
print(x[:4:2])  # ['this', 'the']
print(x[5:])  # ['that', 'called', 'lists']
print(x[::-1])  # ['lists', 'called', 'that', 'type', 'data', 'the', 'is', 'this']

"""Example 1 
Using the "split" string method from the preceding lesson, complete the get_word function to return the 
{n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", 
which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1 """
print("\nExample 1:")
def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]
    return ""


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing


"""String and lists are quite similar since both of them are example of Sequences.
On the sequences data we can executing these methods
    1. Iterating it: for loops
    2. slicing / indexing : list[position]
    3. calculate the value summaries: using len()
    4. concatenate the sequence: list1 + list 2
    5. verifying the sequence elements using 'in'
"""