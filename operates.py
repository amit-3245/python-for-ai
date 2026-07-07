# arithmetic , relational/comparison, assigment, Logical, Bitbase , Membership, identical

#Arithmetic operators(+, -, *,/,%, **)
a = 10
b = 5
print("Arithmetic operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Relational / comparison operators(>, >=, <,<=, ==, !=)
print("Realtional operators")

print(a > b)
print(a < b)
print(a == b)
print(a !=b)
print(a>=b)
print(a<=b)

# Assigment oprators (=, +=, -=)
print("Assigemnt oprator")

x = 10
x = x + 5
x = x - 5
a **=5

print(x)
print(x)

# Logical operators (and, or , not)
print("Logical operators")

var = False
print(not var) # true
print(not (5>8))# true

print((5 > 3) and ( 3 > 2))# true
print((5 > 3) or (3 > 8))


# operator precedence: priority
"""
()
**
*,/,%
+,-

==, !=, >, >=, <, <=

not
and
or

Note if operators has same precedence they can solve left to right
"""