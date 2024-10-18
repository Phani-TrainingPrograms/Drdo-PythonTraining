# Lambda Functions = Short functions that have only one expression. They are small anonymous
# functions that can be defined using lambda keyword and can have one expression statement in it.
# It is created when U want to use the function for a small period of time, like callback
# functions.


# def add(a, b):
#     return a + b

add = lambda a, b : a + b
result = add(13, 12)
print(result)

max_value = lambda x, y : x if x > y else y
print(max_value(14, 6))

is_even = lambda x : x % 2 == 0
age_validation = lambda x : True if x >= 18 else False


print(is_even(20))
print(is_even(19))
print(age_validation(12))
if age_validation(13):
    print("U Can Vote")
else:
    print("U are not 18 to vote")

# Practically, Lambda is used for callback functions, some builtin functions of python that came
# after 3.10 uses these lambdas for filtering, reducing, sorting operations.

grades = [90, 44, 67,55, 67, 89, 26, 67]
passing_grades = list(filter(lambda grade : grade > 60, grades))
#Exercise 1: With the grades, get me the list of all event grades and odd grades.
even_grades = list(filter(lambda x : x % 2 == 0, grades))
print(passing_grades)
print(even_grades)

########################Map Feature in Python
numbers = [1,2,3,4,5,6,7,8,9,10]
my_grades = {}
for grade in grades:
    x = lambda g : "pass" if g > 40 else "fail"
    my_grades[grade] = x(grade)

for key in my_grades.keys():
    print(f"Grade: {key}: Result: {my_grades[key]}")
#
# # my_grades = dict(map(lambda num : "pass" if num >= 40 else "fail" , numbers))
# print(numbers)
# print(grades)
# results = list(map(lambda grade : "pass" if grade > 40 else "fail", grades))
# print(results)
#
# square_numbers = list(map(lambda num : num *  num, numbers))
# print(square_numbers)
#
# #########################Sorting feature in Python#############
users = {"phani" : "apple123", "aditya" : "test123", "kumar" : "myPwd", "ram" : "rma@123}"}
# Sorting the values based on keys:
sorted_users = sorted(users, key = lambda x : x[1])
print(sorted_users)