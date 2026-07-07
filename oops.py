# create class

# class Student:
#     subject = "python"
#     college = "aabc"
#     year = "4rth year"


# a = 10
# stud1 = Student()
# stud2 = Student()
# print(stud1)
# print(stud2)

# print(stud1.college, stud1.subject, stud1.year)
# print(type(stud1))


# Constructor in class
# __init__Method  - use for create an object or initialze an object, its called every time when we create an object of class
# self - is a reference to the current instance of the class, and is used to access variables that belongs to the class 

# class Student:
#     def __init__(self):
#         print("Constructor was called for evry object creation..")

# stud1 = Student()
# stud2 = Student()
# stud3 = Student()

# class Student:
#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = cgpa
    
#     def get_cgpa(self):
#         return self.cgpa

# s1 = Student("Amit", 9.0)
# s2 = Student("Rohit", 9.2)

# print(s1.name)
# print(s1.cgpa)
# print(s2.name)
# print(s2.cgpa)

# print(s1.get_cgpa())
# print(s2.get_cgpa())


# default constructor and parameterized constructor
# default constructor: which has only 1 parameter(self) and it is used to initialize the object with default values.
#e.g
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.cgpa = 9.0
#         self.college = "aabc"

# parameterized constructor: which has more than 1 parameter and it is used to initialize the object with user-defined values.
# e.g
# class Student:
#     def __init__(self, name, cgpa, college):
#         self.name = name
#         self.cgpa = cgpa
#         self.college = college


# class and instance
# class attributes: thats belongs to the class and shared by all instances of the class. It is defined within the class but outside any instance methods.
# instance attributes: its belongs to the object 

# class Student:
#     college_name = "ABC college" # class attribute
#     PI = 3.14 # class attribute

#     def __init_(self, name, cgpa):
#         self.name = name # instance attribute
#         self.cgpa = cgpa # instance attribute
#         self.PI = 3.14 # instance attribute

# stud1 = Student("Amit", 9.0)

# print(stud1.name, stud1.cgpa, stud1.college_name)


class Laptop:
    storage_type = "SSD"   # Class attribute

    def __init__(self, RAM, storage):
        self.RAM = RAM          # Instance attribute
        self.storage = storage  # Instance attribute

    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type = {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        return final_price


# Creating objects
l1 = Laptop("16GB", "512GB")
l2 = Laptop("8GB", "256GB")

# Instance method
l1.get_info()

# Class method
Laptop.get_storage_type()
l1.get_storage_type()

# Static method
final_price = Laptop.calc_discount(100, 10)
print("Final Price =", final_price)