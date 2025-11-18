# Python Exam Question 2

class Student:
    passingMark = 50

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

# This function makes it possible for us to check wether a student 
# has passed or failed based on their mark
    def passOrFail(self):
        if self.mark >= self.passingMark:
            return "Pass"
        else:
            return "Fail"

# Student1 initial grade status
student1 = Student("John", 52)
status1 = student1.passOrFail()
print("Status for ", student1.name, "is", status1)

# Student2 initial grade status
student2 = Student("Jenny", 69)
status2 = student2.passOrFail()
print("Status for", student2.name, "is", status2)

# Updated passingMark 
Student.passingMark = 60

# Status check for student1 after updated passingMark
status1 = student1.passOrFail()
print("Status for ", student1.name, "after updated passingMark is:", status1)

# Status check for student2 after updated passingMark
status2 = student2.passOrFail()
print("Status for ", student2.name, "after updated passingMark is:", status2)
