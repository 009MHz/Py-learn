# Example 1: normal
def perkalian(x, y):
    print("Example 1: Normal")
    print(x * y)


perkalian(8, 5)  # 40

# Example 2: assigning the function result into variable without return
def reduce(x, y):
    print(x - y)


print("\nExample 2: assigning the function result into variable without return")
result = reduce(8, 5)
print(f"Line in seharusnya mengahsilkan 3, tapi ini hasilnya '{result}'")  # None
print(reduce(6, 2))  # 4 & None
'''Kenapa hasilnya None?
    1. Karena hasil yang berupa printing output sudah diambil pada [eromtah sebelumnya]
when called to print in the same time
    2. Akibatnya variable yg diassign tidak akan menghasilkan output apa-apa (None)
'''


# Example 3: Workaround using return
def divider(x, y):
    return x / y


print("\nExample 3: Workaround using return")
divider(91, 3)  # Tidak menghasilkan apa-apa karena output nya berupa value, bukan berupa string
result = divider(34, 5)  # # Tidak menghasilkan apa-apa karena output nya berupa value, bukan string
print(result)  # Ini baruuu bisa -> 6.8
print(divider(22, 7))  # 3.142857142857143
