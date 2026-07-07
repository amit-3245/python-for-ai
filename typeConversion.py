"""
Type conversion : converting one int-> float , float-.int, int->bool
types
1.Type conversion(Implicit python): it done python automatically
2.type casting (explicit python): it need to perform manually
"""

# e.g of implicit python
a = 10
b = 5
print(type(a/b))

# e.g of explicit python): for it we use functions like , int(), float() etc
ans = int(5 + 10.8)
print(type(ans))

val = int("123")
print(type(val))