def sword_cek(weapon):
    jenis = []
    jumlah = 0
    for x in weapon:
        if x.endswith('sword'):
            jenis.append(x)
            jumlah += 1
    return f"Jumlah pedang: {jumlah}, Jenis: {jenis}"


print(sword_cek(['long sword', 'dual sword', 'scimitar', 'bastard sword', 'katana', 'staff']))
print(sword_cek(['scimitar', 'katana', 'staff']))

"""Function Argument and parameter"""
# Argument: value yg diberikan ketika fungsi diberikan (dalam kasus diatas 'weapon')
# parameter: value yg diberikan ketika memanggil fungsi yg memiliki argument -> sword_cek('ini disebut parameter')

"""DEFAULT Values inside the function"""
'example 1: no default'
def add(x, y):
    print (x + y)

add(100,65)

'example 2: assigning 1 default'
# cara baca
def add(x, y=1):
    #cara baca: x = mandatory parameter, sedangkan y optional karena sudah diassgin duluan
    print(x + y)

add(100)  # will be resulted as 101, since there's no assignment pada parameter
add(x=100)

'example 3: assigning 1 default with different parameter'
def add(x, y=1):
    print(x + y)

add(100, 65)  # will be resulted as 165, karena parameter y (65) akan menggantikan 1

"""Error sample"""
#sample 1
def add(x=1, y):
    #SyntaxError: non-default argument follows default argument
    # karena default argument tidak boleh ditaruh di depan (first argument is mandatory)
    print(x + y)

add(5,10)
add(x=3,10)

#sample 2
def add(x, y=1):
    print(x + y)

add(y=65)
# TypeError: add() missing 1 required positional argument: 'x'
# mandatory parameter tidak diberikan sedangkan pada argument, dia ada

#sample 3
def add(x, y=1):
    print(x + y)

add(x=65, 5)
# SyntaxError: positional argument follows keyword argument
# tidak bisa memberikan positional argument setelah memberikan mandatory dipanggil di parameter

