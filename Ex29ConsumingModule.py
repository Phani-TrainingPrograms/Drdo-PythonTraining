# import Ex28Modules ==>Use this for importing the complete module

from Ex28Modules import add_func, greet # Use this syntax for importing few members from the
# module. In this case, U don't need to refer the methods using Module Name.

#result = Ex28Modules.add_func(13,12) ==>When U import the whole module, U must refer the members
# of the module using the ModuleName.MethodName.
result = add_func(23,23)

print(result)

result = greet("Phaniraj")
print(result)

# Try for other functions also