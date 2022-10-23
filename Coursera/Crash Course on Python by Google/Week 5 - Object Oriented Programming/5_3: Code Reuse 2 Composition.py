"""You can have a situation where two different classes are related, but there is no inheritance going on. This is
referred to as composition -- where one class makes use of code contained in another class."""

"Real world concept "
# imagine we have a Package class which represents a software package.
# It contains attributes about the software package like name, version, and size.
# We also have a Repository class which represents all the packages available for installation.
# While there’s no inheritance relationship between the two classes, they are related.
# The Repository class will contain a dictionary or list of Packages that are contained in the repository.

"Example 1: Repository of files"
class Repository:
    def __init__(self):
        # CAUTION: always initialize mutable attributes in the constructor
        self.packages = {}  # dictionary to hold the package object

    def add_package(self, package):
        """adding the object as the parameter"""
        """assign the package name attributes as the key"""
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        """iterating through the package content (dictionary values)"""
        for package in self.packages.values():
            """adding the values size into calculated result"""
            result += package.size
        return result

"""EXPLANATION 
In the constructor method, we initialize the packages dictionary, which will contain the package 
objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every 
instance of the Repository class has its own dictionary. 

We then define the add_package method, which takes a Package object as a parameter, and then adds it to our 
dictionary, using the package name attribute as the key. 

Finally, we define a total_size method which computes the total size of all packages contained in our repository. 
This method iterates through the values in our repository dictionary and adds together the size attributes from each 
package object contained in the dictionary, returning the total at the end. In this example, we’re making use of 
Package attributes within our Repository class. We’re also calling the values() method on our packages dictionary 
instance. Composition allows us to use objects as attributes, as well as access all their attributes and methods. """

"Example 2: Clothing class and accessing the composition"
class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)  # should return 10, since polo & sweatpants using cotton material