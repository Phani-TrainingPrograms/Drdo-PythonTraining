# Magic methods are methods that are invoked automatically and can be customized as UR overriding
# of those methods: __init__ is a magic method of Python. U dont call this method, explicitly,
# but internally called when U instantiate it.

class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def __str__(self):
        return f"{self.name} earns {self.salary}"

    def __eq__(self, other):
        return True if self.name == other.name and self.salary == other.salary else False

# As U create the Employee, UR magic methods get called.
person1 = Employee("Phani", 56000)
print(person1.name)
print(person1)

person2 = Employee("Suresh", 56000)
print(person1 ==person2)