"""Using methods on the strings format"""
'Changing the format'
lorem = "LoReM IpsUm DoLoR sIt aMeT"
lorem.lower()   # Converting into the lower case: 'lorem ipsum dolor sit amet'
lorem.upper()   # Converting into the CAPSLOCK: 'LOREM IPSUM DOLOR SIT AMET'
lorem.title()   # Converting into the titlecase: 'Lorem Ipsum Dolor Sit Amet'

'Removing the whitespace'
lorem = " LoReM "
lorem.strip()   # Removing all the spaces (including the tabs): 'LoReM'
lorem.lstrip()  # Removing all the spaces onm the left: 'LoReM '
lorem.rstrip()  # Removing all the spaces onm the right: ' LoReM'

'Count the text'
lorem = "LoReM IpsUm DoLoR sIt aMeT"
lorem.count('m')    # Counting 'm' character inside the passed variable: 1
lorem.count('r')    # 0
lorem.count('R')    # 2
lorem.count('IpsUm')    # 1
lorem.count('ipsum')    # 0
lorem.lower().count('m')  # Counting 'm' character inside the passed variable after converting it into lower case: 3

'Check the boolean from passed text'
# methods to check the certain texts
fruits = 'Strawberry'
fruits.endswith('berry')    # True
fruits.endswith('ry')       # True
fruits.endswith('apple')    # False
fruits.startswith('Str')    # True
fruits.startswith('str')    # False

# methods to check numbers
fruits.isnumeric()      # Checking the variable is it a number?:False
fruits.isalpha()        # Checking the variable is it a text?: True

"Concatenate the strings"
lists = ["Anuku", "yess", '123', 'kan?']
"".join(lists)      # 'Anukuyess123kan?'
" ".join(lists)     # 'Anuku yess 123 kan?'
'...'.join(lists)   # Anuku...yess...123...kan?'

"Separate the strings into a list"
text = 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'
text.split()    # ['Ut', 'enim', 'ad', 'minim', 'veniam,', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris']

"Example: Creating the acronyms from passed text"
def initials(phrase):
    words = phrase.title()
    result = ""
    for word in words:
        if word.isupper() is True:
            result += word
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS