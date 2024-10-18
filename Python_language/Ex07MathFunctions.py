# math is a std library provided by Python for performing math operations within UR App
import math # U shall use the APIs available in this library.

x = math.pi
y = -4
z = 5

result = round(x)
result = abs(y) # abs gives the no of digits from 0;

result = max(x, y, z)
result = min(x, y, z)

result = math.ceil(x) # rounds a number upwards to its nearest whole no.
result = math.floor(x) # rounds a number downwards to its nearest whole no.

result = math.sqrt(81) # Gets the Square root of a number.

result = math.pow(3, 4) # 3 to the power of 4
# Explore other Functions of math for powerful math operations like logs, calculus operations,
# permutations and combinations.
result = math.perm(8, 5) # no of ways to choose k(5) things from n(8) items.
print(result)

#Exercise 1: #Circumferance of a circle
radius = float(input("Enter the radius of a circle"))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle with radius {radius} is {circumference}")

# Area of a circle : pi* r to the power of 2
radius = float(input("Enter the radius of a circle"))
area = math.pi * pow(radius, 2)
print(f"The area of a circle with radius of {radius} cms is {area} cm²")

# Find the hypotenuse of a Triangle:
a = float(input("Enter the length of Side A: "))
b = float(input("Enter the length of Side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of side C is {c}")

# Exercises at Home:
# Write a program to find an area of a polygon.
# Write a program to print a multiplication table of a number.
# Write a program to convert a Fahrenheit to celsius.




