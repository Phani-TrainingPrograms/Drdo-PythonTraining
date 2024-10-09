# Class: User defined Data type, a Composite Data type that allows to merge multiple kinds of
# data as fields and use them as one unit. It comes with OOP features like Inheritance and
# polymorphism. All the classes are designed based on the Principles of Object Oriented
# Programming called SOLID Principles.
# S : Single Responsibility Principle: One class should do only one job. This concept leads to
# design pattern of layered Architecture.
# O : Open-Closed Principle: A Class once created, is closed for Modification but open for
# Extension. once the Class is created, it is immutable(Cannot be changed). If U want to modify a
# class or add new functionalities to that class, U must extend the class to another using a
# feature called Inheritance and add/modify new features into the newly created class.
# L: Luskov's Substitution Principle. An object of a class can be substituted by any of the
# derived class objects if it does not alter the function signatures. This concept is implemented
# using Runtime polymorphism feature.
# I :Interface segregation Principle: When U create interfaces, U should create simple and less no
# of methods for it and dont make a big interface and expect a class to implement all of them.
# D: Dependency Inversion principle: It is better to associate an object to its abstractness
# rather than the concreteness.

#Every member function shall have one default parameter called self which implies the referece of
# the object that we are using with. Equivalent to this operator in C++, Java and C#.
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_details(self):
        print(f"The name is {self.name} is from {self.address} and can be contacted by {self.phone}")

# Every variable of the UDT Class is called as Object. This object must be instantiated using ()
# operator. Internally, it shall call the __init__ function  which will assign the values to the
# fields of the class and make it available. Fields are members of the class which represents the
# data associated with the class. __init__ is a method that is called automatically when the
# object is created. Similar to Constructor concept of OOP.
person = Person(name="Phaniraj", phone=9945205684, address="Bangalore")
person.display_details()
print("The name of the Person is " + person.name)

########################Creating Private members in Python######################
class Student:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob
    # Python does not directly support the OOP concepts like Private or Public members. All are
    # public members. If U want to achieve private scope for U members, Python allows to use a
    # convention with __ as prefix to UR members. This is applicable for both member variables as
    # well as member Functions. As the members U Created dont have access outside the class,
    # U should provide public accessors in the form of properties or functions to set or get the
    # data. This is similar to properties of C# and getters/setters of Java.
    def get_name(self):
        return self.__name
    def get_birth_date(self):
        return self.__dob

new_student = Student("Phaniraj", "01/12/1976")
new_student2 = Student("Mahesh", "12/05/1980")

print(f"The Name is {new_student.get_name()} and his Date Of birth is {new_student.get_birth_date()}")


print(f"The Name is {new_student2.get_name()} and his Date Of birth is {new_student2.get_birth_date()}")
# A Class definition is like a blue print and objects are real data for those classes.