"""Changed the string inside the text"""
# example 1: changing text directly
'context: changing the kong with a long'
message = 'A kong string with a silly typo'
#message[2] = 'l'
# resulted as an error since the string is immutable (can't be changed directly using assignment)
# TypeError: 'str' object does not support item assignment
'solutions'
new_message = message[0:2] + 'l' + message[3:]
print(new_message)  # A long string with a silly typo

# example 2: getting the character position inside the text
pet = 'Cats & dogs'
pet.index('&')
# getting the "&" position inside the pet -> 5
# using the .index method to use the function
# method is a function associated with a specific class
# to use it we need following the format: variable".called_method()"
pet.index('C')  # -> 0
pet.index("dog")  # 7
pet.index('s')  # 3
# returning the first position of "s" although there's 2 position inside the variable
#pet.index("Dog")
# returned as error since Dog is not available
# ValueError: substring not found
'solutions to avoid the previous error'
# Check the value using the keyword in before the variables
"Dragons" in pet    # False
"Cats" in pet   # True
"dog" in pet    # True
"Dog" in pet    # False

# example 3: The real situations using this method
"""
1. Our company has moved to using a new domain
2. all the employees email address will using the new domain format
3. most of the employees still using the old domain
4. your job is writes a program that replaces this old domain with the new one
"""

print("example 3: The real situations using this method")
# todo 1: define the function that replace the domain that accepts 3 arguments
def replace_domain(email, old_domain, new_domain):
    # Todo 2: check the keyword inside the email is correct (@old_domain)
    if "@" + old_domain in email:
        # Todo 3: iterates the elements inside the old domain by taking the incorrect email format (the old domain)
        index = email.index("@" + old_domain)
        # Todo 4: Create the new email, by take out the incorrect format and replacing with the new one
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email