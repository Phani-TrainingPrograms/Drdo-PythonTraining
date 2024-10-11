# Decorators are a powerful tool to allow U to modify or extend the behavior of a function
# without permanently modifying the function itself.
# A Decorator is a function that takes another function as argument(CALLBACK FUNCTIONS) and then
# call this function inside this function before returning it back.
# Logging any function calls
# validating inputs before calling the method
# Performance Monitoring.
# Authentications and Authorizations.


def my_func_formatter(func):
    def wrapper(*args):
        print("###############")
        func(*args)
        print("###############")
    return wrapper

@my_func_formatter
def say_hello(arg):
    print("Hello")

say_hello("")

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
    return wrapper


@my_func_formatter
@logger
def add_func(a, b):
    return a + b

add_func(4, 5)
