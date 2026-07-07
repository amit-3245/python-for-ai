# marks = [98,79,100, 65,92]

# print(marks)
# print(len(marks))
# marks[2] = 70

# print(marks)
# print(type(marks))
# print(marks[-5:-2])


# list methods

nums = [1, 2, 3]

nums.append(4) # add one element at the end
print(nums)

nums.insert(2, 10) # insert 10 at index 2
print(nums)

nums.sort(reverse = True) # sort the list in descending order
print(nums)

nums.reverse() # reverse the list
print(nums)



# loops in list

l = [1, 2, 3, 4, 5]
for i in l:
    print(i)


x = 10
indx = 0

for val in l:
    if val == x:
        print("found at index", indx)
        break
    indx += 1
    
