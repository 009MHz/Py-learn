"""You can have a situation where two different classes are related, but there is no inheritance going on. This is
referred to as composition -- where one class makes use of code contained in another class. For example, imagine we
have a Package class which represents a software package. It contains attributes about the software package,
like name, version, and size. We also have a Repository class which represents all the packages available for
installation. While there’s no inheritance relationship between the two classes, they are related. The Repository
class will contain a dictionary or list of Packages that are contained in the repository. Let's take a look at an
example Repository class definition: """