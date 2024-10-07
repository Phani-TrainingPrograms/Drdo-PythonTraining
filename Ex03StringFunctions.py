# string is a class in Python that comes with functions that help in transforming the values
# based on the User requirement.

name = "phani raj"
# No of charecters in the string: len
print(len(name))
print(name.capitalize())
# Capitalize every word in a string:
print(name.title())

print(name.upper())

#Find out if the string has a number:
print(name.isdigit())
#Find out if the string has only alphabets:
print(name.isalpha())
#Find out a character in string:
print(name.find('a'))
#Find and replace
print(name.replace('a', 'aa'))


# print(dir(name))
# help(type(name))

# Every variable internally is an object in python. It has a method called id which could be used
# to identify the object. It is purely for understanding purpose.
num = 123
print(id(num))