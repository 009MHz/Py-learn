"Built in Class Example"
type(7)  # <class 'int'>
type("hi")  # <class 'str'>

"Built in Methods example"
# isupper()
# upper()

"""Up till now what we used inside the string type is called an instance
instance: the contents that exist when we're using the method inside the class
To check the attributes & methods in specific classes we can use dir() function
"""
# Check the dir() content on string type
print(dir(''))
"""['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] """

# Check the dir() content on list type
print(dir([]))
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', 
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
'reverse', 'sort'] """

"""
Special method: The first given values is started & ended with double underscore (__method__)
Normal methods: any value that we've been use before
To show the documentation of corresponding classes we can use help('str') function
"""
#help(__add__)  # NameError: name '__add__' is not defined. Did you mean: '__name__'?
help('__add__')  # No Python documentation found for '__add__'.
help("")   # Help on class str in module builtins: ...
help(0)  # Help on int object: ...
help({})  # Help on dict object:...