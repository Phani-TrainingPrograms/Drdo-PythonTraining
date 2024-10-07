# variables = A Containers for a value. It behaves like the value that it contains.
# strings are the way to store characters in Python. All inputs and outputs
# shall be strings. U may have to convert to other data types if U want to do some
# calculations.
# python supports strings, numbers, floating values, booleans, objects(user defined data types), None.
################String data types#####################################
name = "Phaniraj" # variable in Python.
print(name) # don't use the "" while using the variables.

name = 'Phani' # variables allow to change the value any time in the course of the program.

# If a variable has 2 or more words, U should seperate them using _
first_name = "Phani"
last_name = "Raj"
full_name = first_name + " " + last_name
print(full_name)
print(f"{first_name} {last_name}")

# If U want to know the kind of data that UR variable is using, we can use type function.
print(type(full_name)) # the data type is string.

########################int data type###############################
age = 47
# We use other data types only if we are computing any mathematical functionality.
# years = 34
print("The data type of age is " + str(type(age)))
# age += years # same as age = age + 1
print(age)
# integers hold only whole numbers.
# converting the int to string using str(int). This is called as type casting.
print("UR age is " + str(age)) #old style
print(f"UR age is {age}") # new style using f(ormat) string.

#########################float data type###########################
height = 23.45 # decimal values we use floats.
print(height)
print(type(height)) # <class 'float'>
print("YOUR HEIGHT IS " + str(height) + " inches")
print(f"Your height is {height}") # No need to typecast

#####################boolean data type###############################
is_male = True # True, T is uppercase.
print(is_male)
print(type(is_male))
print(int(is_male)) # use int() to typecast to int so that U can evaluate it to 0 or 1.

###############Important points#######################
'''
Naming conventions:
lowercase, underscore_between_words, 
should not start with numbers. 
There is no specific type for numbers and floats. A variable could hold either
Python allows extremly large values for numerical without loosing any precision 
Strings with "" or '' are same. Its only a matter of convenience. 
Bool values should be True or False and is case sensitive.
All conventions and coding stds are defined by PEP(Python Enhancement Proposal). Currently it is PEP 8 
If a variable is declared but not assigned, it is None. In the context of the boolean it is False. 
'''

name, age, attractive = 'phani', 47, True
print(f"{name} is of {age} years and his/her personality is {attractive}")

phani = rajan = ram = 47
# all the variables will have the same value
print(f"{phani}, {rajan} {ram}")
