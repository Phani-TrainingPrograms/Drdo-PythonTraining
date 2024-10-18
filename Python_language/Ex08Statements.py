#if: Do some code only if some condition is TRUE or FALSE, else do another thing.

age = int(input("Enter the age for applying UR Credit card: "))

# check for the validation:
if age >= 50:
    print("U R too old to sign up")
elif age >= 18:
    print("U R now signed up!!!")
elif age < 0:
    print("U R not even born!!!!")
else:
    print("U must be 18+ to sign up")

###################Important points#################################
'''
Python relies on indentation to define the scope. 
elIf: If the previous conditions are not true, then try this condition. 
the if or elif  should match for a boolean expression.  
else isn't mandatory block. 
'''

###############Ternery operations in Python########################
num, a, b = 5, 6, 7
print("Positive" if num > 0 else "Negative") # Simple way of writing if..else in a single line.
print("Even" if num % 2 == 0 else "Odd")
# Get the max value and min value from the 2 variables in a single line for each operation.
max_num = a if a > b else b
min_num = a if a < b else b
print(f"{max_num} and {min_num}")


