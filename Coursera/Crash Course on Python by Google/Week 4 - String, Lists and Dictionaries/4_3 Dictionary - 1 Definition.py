"""
- Dictionary is used to organize elements into collections
- Unlike lists, you don't access elements position inside dictionaries using their position
- The data inside dictionaries take the form of pairs of keys and values
- To get dictionary value we use its corresponding key
- While the list index is must be a number, we can assign any data type into as a keys
"""

"Example 1:"
x = {}
type(x)  # output: <class 'dict'>
file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, "py": 23}
print(file_counts)  # -> {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

# case 1: getting the values under the given key
file_counts['csv']  # -> 2

# Case 2: using the key to check the boolean
'jpg' in file_counts  # -> True
'mkv' in file_counts  # -> False

# Case 3: adding new keys & values inside the dictionary
file_counts['cfg'] = 8
print(file_counts)  # {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}

# Case 4: updating new values based on existing key
file_counts['csv'] = 21
print(file_counts)  # {'jpg': 10, 'txt': 14, 'csv': 21, 'py': 23, 'cfg': 8}

# Case 5: Removing the key & its value
del file_counts['cfg']
print(file_counts)  # {'jpg': 10, 'txt': 14, 'csv': 21, 'py': 23}

"Example 2"
print("\nExample 2")
"""The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	
1) Add an entry for Epilogue on page 39. 	
2) Change the page number for Chapter 3 to 24. 	
3) Display the new dictionary contents. 	
4) Display True if there is Chapter 5, False if there isn't."""

toc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
___  # Epilogue starts on page 39
___  # Chapter 3 now starts on page 24
___  # What are the current contents of the dictionary?
___  # Is there a Chapter 5?

