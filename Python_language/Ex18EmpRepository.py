# We need a class to represent each employee of an organization
# We need a class that holds all employees of an organization. This class is usually called as
# REPOSITORY Class. This class shall have private data and functions to manipulate the data and
# most of the time, the functions are CURD operations: Crate, Update, Read and Delete.



class Employee:
    def __init__(self, id, name, address, salary):
        self.id = id
        self.address = address
        self.salary = salary
        self.name = name

class EmpRepository:
    def __init__(self):
        self.__emp_list = [ Employee(123, "Phaniraj", "Bangalore", 56000)]  # EmpRepo has an array
        # of employees in it.

    def add_employee(self, emp):
        self.__emp_list.append(emp)

    def get_all_employees(self):
        return self.__emp_list

    def get_employee_by_id(self, id):
        for emp in self.__emp_list:
            if emp.id == id:
                return emp

    def delete_employee(self, emp):
        self.__emp_list.remove(emp)

    def update_employee(self, emp):
        rec = self.get_employee_by_id(emp.id)
        if rec is not None:
            rec.id = emp.id
            rec.name = emp.name
            rec.address = emp.address
            rec.salary = emp.salary

drdo_employees = EmpRepository()
def display_feature():
    data = drdo_employees.get_all_employees()
    for rec in data:
        print(f"Name: {rec.name} from {rec.address}, \nSalary: ₹ {rec.salary :.2f}. \nHis Id is"
              f" {rec.id}")
    return True

def finding_feature():
    id = int(input("Enter the Id of the Employee to Search: "))
    rec = drdo_employees.get_employee_by_id(id)
    if rec is not None:
        print(f"Name: {rec.name} from {rec.address}, \n Salary: ₹ {rec.salary :.2f}. \n His Id is"
              f" {rec.id}")
    else:
        print("No matching record found to display")
    return True

def adding_feature():
    id = int(input("Enter the new ID of the Employee: "))
    name = input("Enter the name of the new Employee: ")
    address = input("Enter the Address of the Employee: ")
    salary = int(input("Enter the Salary for this Employee"))
    empObj = Employee(id, name, address, salary)
    drdo_employees.add_employee(empObj)
    return True


def updating_feature():
    id = int(input("Enter the ID of the Employee to Update: "))
    name = input("Enter the new name of the Employee: ")
    address = input("Enter the new Address of the Employee: ")
    salary = int(input("Enter the new Salary for this Employee"))
    empObj = Employee(id, name, address, salary)
    drdo_employees.update_employee(empObj)
    return True


def deleting_feature():
    
    return True
def print_menu():
    print("#####################EMPLOYEE MONITORING SYSTEM##################")
    print("To View All Employees: PRESS 1")
    print("To Find An Employee: PRESS 2")
    print("To Register New Employee: PRESS 3")
    print("To Update An Employee: PRESS 4")
    print("To Delete An Employee: PRESS 5")

def process_menu(choice):
    match choice:
        case "1":
            return display_feature()
        case "2":
            return finding_feature()
        case "3":
            return adding_feature()
        case "4":
            return updating_feature()
        case "5":
            return deleting_feature()
        case _:
            print("Invalid Choice, Please try again")
            return True
is_processing = True
while is_processing:
    print_menu()
    choice = input("Enter the choice as [1-5] or q To Quit: ")
    if choice.lower() == 'q':
        break
    is_processing = process_menu(choice)


