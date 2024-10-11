# File Reading writing is done using the built in global methods
'''
File Modes for read/write the files:
w : writing, overwrites if the file exists.
r : reading mode, Default mode
a : append mode: Appends the file and the data is added at the end of the file.
x : Exclusive creation, creates a new file and writes to it, if the file exists raises an Exception
t : Text mode, opening the file as text file.
+ : wild character for both reading and writing.
'''
from xml.etree.ElementTree import indent

#####################writing a text file#####################
file_name = "SampleFile.txt"
try:
    with open(file_name, 'x') as file:
        file.write("Hello world from Python into a file")
        print(f".txt file '{file_name} has been created successfully")
except FileExistsError as err:
    print(f"Error Details: {err}")
except Exception as genEx:
    print(f"Unknown error: {genEx}")

#######################Writing Json data##########################
# JSON: Javascript object Notation.
import json # for Json file operations

empRecord = [{
        "empId":123,
        "empName":"Phaniraj",
        "empAddress":"Bangalore",
        "salary":45000
},
{
    "empId" : 124,
    "empName":"ramanth",
    "empAddress":"Lucknow",
    "salary":40000
}
]

file_name = "empRecords.json"
try:
    with open(file_name, "w") as file:
        json.dump(empRecord, file, indent=4)
        print(f"Json data stored successfully")
except FileExistsError as err:
    print(f"{err}")
##################Converting an List of Employees to JSON file#############################
class Customer:
    def __init__(self, name, address, bill):
        self.cstname = name
        self.address = address
        self.bill = bill

    def to_dict(self):
        return { "cstname" : self.cstname, "address" : self.address, "bill" : self.bill}

def writeJsonFile(jsondata, fileName):
    try:
        with open(fileName, 'w') as file:
            json.dump(jsondata, file, indent=3)
    except Exception as e:
        print(f"{e}")

customers = [Customer("Phaniraj", "Bangalore", 4900), Customer("Phaniraj", "Bangalore", 4900),
             Customer("Phaniraj", "Bangalore", 4900),Customer("Phaniraj", "Bangalore", 4900),Customer("Phaniraj", "Bangalore", 4900)]
# todo: Create a Repo class that has the CURD operations in it which saves the data to a jsonfile.

jsonObjects = [cst.to_dict() for cst in customers]

json_data = json.dumps(jsonObjects)

writeJsonFile(jsonObjects, "Customers.json")



