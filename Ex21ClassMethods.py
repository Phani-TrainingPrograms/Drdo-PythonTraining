# Methods that belong to a class but not to any instance is called as classmethods. Works like
# Static methods of other programming languages.

class Student:
    count = 0
    total_gpa = 0.0

    def __init__(self, name, gpa):
        self.student_name = name
        self.student_gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


    def get_student_info(self):
        return f"{self.student_name} {self.student_gpa} and the student count is {Student.count}"

    @classmethod
    def get_count(cls):
        return  f"The total no of Students are {cls.count}"

    @classmethod
    def get_all_gpa(cls):
        return f"The Total GPA of the Students in the college is {cls.total_gpa}"

    @classmethod
    def get_avg_gpas(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count}"

s1 = Student("Phaniraj", 6.8)
print(s1.get_student_info())
s2 = Student("Ramesh", 7.8)
print(s2.get_student_info())
s3 = Student("Adithya", 9.8)
print(s3.get_student_info())
s4 = Student("HariOm", 5.8)
print(s4.get_student_info())

print(Student.get_count())
print(Student.get_all_gpa())

print(Student.get_avg_gpas())

