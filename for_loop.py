# string = "Hello"

# in => membership operator

# for var in string:
#     print(var)
#     print(len(string))

# check o in string

# string = "Hello"

# if 'o' in string:
#     print("o exists in string")


#print hello world 5 times using for loop

# for i in range(5):
#     print("hello world")

# count no. of i in given string
# count = 0
# word = "artificial intellegence"

# for ch in word:
#     if ch == 'i':
#         count += 1

# print("count of i =", count)

# print vowel count of a given strings.

# word = "artificial"
# count = 0

# for ch in word:
#     if(ch == 'a' or  ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count +=1

# print("ans =", count)


# range(start, stop, step)
# range(5) means 0,1,2,3,4

# for i in range(5):
#     print(i)


# for i in range(1,6):
#     print(i)

# print odd numbers 1 to 10

# for i in range(1, 10, 2):
#     print(i)


# print sum of n natural numbers  = n(n + 1)/2

n = int(input("enter number:"))

sum = 0

for i in range(1, n + 1):
    sum +=i
print("sum=",sum)