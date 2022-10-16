"""**kwargs is collecting passed parameter and creating new variable as kwargs and return as dictionary"""
#example 1: using **kwargs as argument
def name(**kwargs):
    print(f"Default **kwargs result: {kwargs}")

name(name='Me', origin='Jogja', age= 22)  # {'name': 'Me', 'origin': 'Jogja', 'age': 22}
name(id=['Me, 22'], city=['Jogja'])  #{'id': ['Me, 22'], 'city': ['Jogja']}
# name('Me', 22)  #TypeError: name() takes 0 positional arguments but 2 were given

#example 2: using ** to unpack the passed parameter
def named(id, age):
    print(f'Example 2 result: name = {id} | age = {age}')

sample2 = {'id': 'Me', 'age': 22}
named(**sample2)  # Example 2 result: name = Me | age = 22
named(sample2)  #TypeError: name() takes 0 positional arguments but 1 was given
named(sample2, 20)  #TypeError: named() missing 1 required positional argument: 'age'


#example 3: Combing *args and **kwargs
def both(*args, **kwargs):
    # both function is receiving multiple values
    # *args can be receiving many number of values separated with commas
    # **kwargs can be receiving many values in dictionary types