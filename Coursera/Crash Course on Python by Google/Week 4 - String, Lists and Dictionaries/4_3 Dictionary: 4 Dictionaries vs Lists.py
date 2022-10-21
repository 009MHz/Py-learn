""" When we pick the correct method for different scenario
List:
    - better to use when we have information we'd like to collect
    - Can store any data types (str, int, float)
        example: Storing a series of IP addresses for connected users
        ip_addresses = ['192.168.1.1', '127.0.0.1', '8.8.4.4']

Dictionaries:
    - better to use if we want storing for a specific elements
    - can store any data types, but for the keys, it's only accepted specific type
        Example:
        host_addresses = {'router: '192.168.1.1', "localhost": '127.0.0.1',
        "google": '8.8.4.4'}
"""

"Example 1"
"""In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be 
a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their 
colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", 
"blue shirt", and so on. """
wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for x in wardrobe:
    for y in wardrobe[x]:
        print("{} {}".format(y, x))


