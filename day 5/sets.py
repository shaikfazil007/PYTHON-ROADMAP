# #sets


# e = set()  #creates an empty set

# s = { 1 , 2, 3, 1, 1, 8 }
# print(s)   #does not print repeated values


s = { 1 , 2, 3, 1, 1, 8,"fazil" }
a = s.add(56)
print(s,type(s))
s.remove(3)
print(s)

s1 = {1, 2, 4, 12}
s2 = {4, 2, 16, 1}
print(s1.union(s2))
print(s1.intersection(s2))
