'Example Case: Creating Pokemon Tables'
# instead creating ASCII table, check the created module here: https://pypi.org/search/?q=prettytables&o=
from prettytable import PrettyTable  # importing the Class inside the module
tab = PrettyTable()  # assigning the class into called variable

"Using the method (function inside the class)"
#metode 1
tab.field_names = ["Pokemon Name", "Elements"]  # argument needed: any value as the header
# argument needed: list of 2 values (mengikuti headernya) separated by comma
tab.add_rows(
    [
        ["Chespin", "Grass"],
        ["Pikachu", "Electric"],
        ["Golduck", "Water"]
    ]
)
print(tab)

#metode 2
tab.add_column("Pokemon Name", ["Lucario", "Ralts", "Bulbasaur"], 'l')
# argument needed Column Title, isi column, text alignment
tab.add_column("Elements",["Steel", "Psychic", "Grass"], 'l')
print (tab)

#metode 3: Invalid argument
'memberikan jumlah input yg tidak sesuai dengan argument yg diminta'
tab.add_column("Pokemon Name", ["Lucario", "Ralts", "Bulbasaur"], 'r')
tab.add_column("Elements",["Steel", "Psychic",])
print (tab)
# ValueError: Column length 2 does not match number of rows 3
# karena data di column selanjutnya tidak sesuai element 2 column, name 3 column