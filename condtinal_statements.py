# Conditional Statements: if, elif, else, nested if

# if condition
age = 21
if age >= 18:
    print("You can vote")
    print("You can drive")


# else condition
age = 22
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")


# elif condition
color = input("Enter color: ")

if color == "red":
    print("Stop")
elif color == "green":
    print("Go")
elif color == "yellow":
    print("Look")
else:
    print("Invalid color")