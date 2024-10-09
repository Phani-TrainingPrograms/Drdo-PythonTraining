# Abstract class: A Class that has one or more methds that are not implemented, but is expected to be implemented by the child classes. Abstract classes are imported from the ABC module and then used in the program.
from abc import ABC, abstractmethod

class Account(ABC):# This is an Abstract class in Python
    def __init__(self, id, name, initial_amount):
       self.account_no = id
       self.account_name = name
       self.balance = initial_amount

    @abstractmethod
    def calc_interest(self):
        pass

class SBAccount(Account):
    def __init__(self, id, name, initial_amount):
        super().__init__(id, name, initial_amount)

    def calc_interest(self):
        # todo: implement the method
        print("calc interest implemented here")

acc = SBAccount(123, "Phaniraj", 5000)
acc.calc_interest()
# Abstract classes are incomplete classes as one or more methods of it is not implemented. So U cannot instantiate an Abstract class.
# acc = Account(123, "Phaniraj", 5000)

