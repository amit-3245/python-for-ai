#Polymorphism: many forms
# 1. function overriding(inheritance)
# 2. function overloading

# 1. function overriding(inheritance)

# class Employe:
#     def get_destignation():
#         print("designation = Employe")

# class Teacher(Employe):
#     def get_destignation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_destignation()


#Duck Typing

class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()

