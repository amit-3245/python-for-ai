s = {1, 2, 3, 4, 5}

empty_set = set()
print(type(empty_set))
print(empty_set)

s.add(9)
s.remove(1)
s.clear()
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))
print(s1.intersection(s2))