# Input() = A Function that prompts the user to enter the data. This function waits for the user to make an entry and returns that value. The value can be stored into a variable.
# All inputs that come into the system shall be strings. U must convert the inputs to your respective data types and make the computations.

name = input("Enter the Name: ")
print("The Name entered is " + name)
age = int(input("How old are you?: "))
print(f"You are {age} years old")
print(type(age))
years = int(input("Enter the no of years U want to work: "))
age += years
print(f"U will be working till {age} years of your age. ")


