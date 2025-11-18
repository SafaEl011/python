#Python Exam Question 1

# This class helps us store first name, last name and age from a person
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)

# This class helps us store the values from person, AND new ones that are
# specifically unique to students (student_id)
class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        super().__init__(fname, lname, age)
        self.student_id = student_id

    def get_stuinfo(self):
        super().get_info()
        print("Student ID:", self.student_id)

# This class helps us store the values from person, AND new ones that are
# specifically unique to employees (emp_no & salary)
class Employee(Person):
    def __init__(self, fname, lname, age, emp_no, salary):
        super().__init__(fname, lname, age)
        self.emp_no = emp_no
        self.salary = salary

    def get_empinfo(self):
        super().get_info()
        print("Employee No:", self.emp_no)
        print("Salary:", self.salary, "USD")


#This code is to check if the classes work properly
new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo()
print("==========================")
new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
new_employee.get_empinfo()
