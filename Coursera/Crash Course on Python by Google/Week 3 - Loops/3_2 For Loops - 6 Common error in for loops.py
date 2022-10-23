"""example 1: TypeError: 'int' object is not iterable"""
# for x in 25:
#     print(x)
    # reason: 25 berlaku sebagai angka tunggal atau bukan range
    # angka tunggal tidak akan bisa di iterate (dibongkar)

'solutions: ganti menjadi range'
for x in range(25):
    print(x)

"""example 2: looping single value"""
print("\nexample 2: looping single value")
for x in [25]:
    print(x)
    # bukan error, tapi cuman ga make sense
    # isinya cuman satu dan ga perlu di-iterate

"""example 3: iterating the string"""
print("\nexample 3: iterating the string")
def greetings(friends):
    for x in friends:
        print("Hi " + x)


greetings(['Taylor', "Luisa", "Ron", "Granger"])  # normal
greetings("Amy")  # Hi A, Hi m, Hi y (upnormal)
# reason: karena string itu iteratable (bisa dibongkar)
# passed parameter akan dibongkar and returned one by one

"""example 4"""
print("\nExample 4")
"""The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is 
one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling 
it like in this example, something is not right. Can you figure out what to fix? """
def validate_users(users):
    for user in [users]:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users("purplecat")