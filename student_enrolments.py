"""
Given a list of tuples with info(name, subject):
list all unique course
list student enrolled in English
create dictionary ( student , set of courses)
"""

from os import name


info = [
    ("Amit", "Python"),
    ("Rohit", "java"),
    ("Mohit", "English"),
    ("Shivam", "Python"),
    ("Rohit", "English"),
    ("Amit", "java"),
    ("Shivam", "English"),
]
# list all unique course
course_set =set()
for tup in info:
    print(tup)
    print(tup[0])
    print(tup[1])

print(course_set)

# list student enrolled in English
print("Students enrolled in English:")
for name, course in info:
    if course == "English":
        print(name)
        

# create dictionary ( student , set of courses)
student_courses = {}

for name, course in info:
    if(student_courses.get(name) == None):
        student_courses.update({name: set()})
        student_courses[name].add(course)
    else:
        student_courses[name].add(course)
print(student_courses)


 