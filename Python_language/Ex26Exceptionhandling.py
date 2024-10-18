# Exceptions raised by the Python interpretor will be handling using try..except...else...finally
# block.
# try block: lets U test the block of code for any errors.
# except: block will allow U to handle the Exceptions that are raised in the try block.
# else: lets U execute the code when there is no error
# finally: lets U execute the code regardless of the result of try---except blocks.
# U can have multiple except blocks for a given try. Python has built- in exceptions that can be
# used to catch multiple kinds of exceptions.
from xml.dom import ValidationErr

try:
    print(sample)
except NameError:
    print("Variable sample is not defined")
except:
    print("Unknown Error occurred")

def div_numbers(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as ex:
        print(f"The Following error occured: {ex}")
    # except TypeError:
    #     print("The Data type is invalid")
    except Exception as e:
        print(f"Unknown Exception has occured: {e}")
    else: # Excecutes only on success condition
        print(f"Result: {result}")
    finally: # Executes on all conditions, clean up operations.
        print("Execution completed!")

div_numbers(10, 5)
div_numbers(10, 0)
div_numbers(5, "apple")

#######################how to raise exceptions##################################
def check_for_even_number(num):
    if num % 2 == 0:
        return True
    else:
        raise ValueError("Numbers cannot be odd nos")

try:
    print(check_for_even_number(11))
except ValueError as e:
    print(f"Exception caught: {e}")
#########################Custom Exception class#####################
# Custom Exceptions in Python are classes derived from Exception, the base class for all kinds of
# Exceptions.
class EmployeeNotFound(Exception):
    def __init__(self, message):
        self.message = message

def find_employee(id):
    if id < 35:
        print(f"Employee found with ID {id}")
    else:
        raise EmployeeNotFound(f"Employee with Id {id} not found!!!!")

try:
    find_employee(46)
except EmployeeNotFound as e:
    print(f"{e}")
else:
    print("Employee found successfully, shall share the details shortly")
finally:
    print("Application exited gracefully")

### Summary:
# - You can handle multiple exceptions using multiple `except` blocks or by combining exceptions in a tuple.
# - Use the `else` block for code that runs when no exceptions occur.
# - The `finally` block is always executed, useful for cleanup tasks.
# - try must be followed by either except, or finally block.
# - except: can be excluded if U have a finally block.
# - else: Entirely optional and can be excluded.
# - finally: Optional, but required if no except block, and usually used for clean_up tasks.


