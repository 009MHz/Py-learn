"""
Strings: Sequences of characters and 'immutable', using "" or '' to hold the characters
Lists: Sequences of elements of any type and are 'mutable', using [] to hold the values
Tuple: Sequences of elements of any type and are 'immutable', using () to hold the values
"""

"""Why tuple is needed?
Because Lists are mutable, kita ga pisa pakai ini untuk menyimpan suatu value yg sifatnya berpasangan 
(e.g: user name dan user ID)
"""

fullname = ('Grace', 'M', 'Hopper')
# variable ini menyimpan nama yg terdiri dari: first name, middle name, dan last name
# in the future, modifying this type is not allowed, so that's why we're using tuple instead of lists
# The position of the elements inside the tuple have their own meaning

"Example 1: the seconds converter function"
print("Example 1: the seconds converter function")
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining


converter = convert_seconds(4300)
type(converter)  # <class 'tuple'>
print(converter)  # output: (1, 11, 40)
# since the elements is tuple the order of the elements have their meaning
# 1 is represented the hours
# 10 is represented the minutes
# 40 is represented the seconds

"""since we're using tuples, we can unpack or destroying the values inside it on by one and the variable will be holding
the values based on given index"""
# Example 2: unpacking/destroying the tuple
print("\nExample 2: unpacking/destroying the tuple")
waton1, nganu, luweh = converter
print(nganu)  # 11
print(luweh, waton1)  # 40  1

"Example 3: Tuples to store information on file"
print("\nExample 3: Tuples to store information on file")
def file_size(file_info):
    file_name,extension,size = file_info
    return("{:.2f}".format(size / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21




