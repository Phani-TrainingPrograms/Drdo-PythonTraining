from abc import ABC, abstractmethod

class FatherClass(ABC):
    def __init__(self, title):
        self.company = title

    def make_payment(self, mode, amount):
        if mode == "cash" or mode == "cheque":
            print(f"A payment of ₹{amount:.2f} is made thru' {mode}")
        else:
            print("Other modes of payment not accepted")
    @abstractmethod
    def recieve_payment(self, mode, amount):
        pass

class SonClass(FatherClass):
    def recieve_payment(self, mode, amount):
        if mode == "cash" or mode == "upi":
            print(f"A payment of ₹{amount:.2f} is received thru' {mode}")
        else:
            print("Other modes of payment not accepted")

    def __init__(self, title):
        super().__init__(title) # Refers to immediate base class and is requierd when U want to call the base class's init to set the values to the base class
        self.company = title
    def make_payment(self, mode, amount):
        if mode == "cash" or mode == "upi":
            print(f"A payment of ₹{amount:.2f} is made thru' {mode}")
        else:
            print("Cheque payments not accepted")

business = SonClass('SBC Provisions')
print(business.company)
business.make_payment("upi", 6000)