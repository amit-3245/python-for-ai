# string is a sequence  of characters
# word = "python"
# word2 = "Hello"

# print(word)
# print(len(word))

#concatinate
# print(word + " " + word2)
 # and other way to concatinate

# result = word + " " + word2
# print(result)
 # and ohter way to concatinate

# print(word, word2)

# indexing
# print(word[0])

# loop in string
# word = "python"

# for ch in word:
#     print(ch)


# operators in string

# slicing

word = "python"
# print(word[2:4])
# print(word[2::])
# print(word[::2])
# print(word[:])

# print(word[-1])
# print(word[::-1])

#string formatting

# for it we have two ways
# format()
# f-string

# format()
a = 5
b = 10
sum = a + b
print("language is {}".format("python"))
print("sum is {}".format(a, b, sum))

# index based formatting
print("sum of {0} and {i} is {2}")

#value based formatting
print("values of vars {a} & {b}".format(a=5, b=10))

# f-string
a = 5
b = 10
print(f"sum of {a} and {b} is {a + b}")