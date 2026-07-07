#List Comprehension
#  syntax
#new_list = [expression for item in iterable]

# nums = [-2, -3, 3, 4, 4,-1,7]

# nums = [0 if val < 0 else val for val in nums]
# print(nums)


# squares = [i * i for i in range(1, 6)]
# print(squares)


# numbers = [1, 2, 3, 4, 5]
# double = [x * 2 for x in numbers]
# print(double)


#With if condition
# numbers = [1, 2, 3, 4, 5,6]

# even = [x for x in numbers if x % 2 == 0]
# print(even)
squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]