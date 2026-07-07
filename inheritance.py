# # Inheritance
# # Reusing attr & methods from a parent (base) class
# """
# typesa of inheritance
# 1. single level inheritance
# 2. multi level inheritance
# 3. multiple inheritance

# """
# class Employe:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self, new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employe):
#     def __init__(self, subject):
#         self.subject = subject
    

# t1 = Teacher("Math")
# t1.change_time("5pm")

# class AdminStaff(Employe):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init_(role)
#         self.salary = salary

# acc1 = Accountant(25000, "CA")


# print(t1.subject, t1.start_time, t1.end_time)

# Multiple Inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)      # Calls Teacher constructor
        Student.__init__(self, gpa)   # Calls Student constructor
        self.name = name


ta1 = TA(15000, 9.3, "Sharma")

print(ta1.name, ta1.gpa, ta1.salary)