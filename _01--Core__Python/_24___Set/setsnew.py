a = {2,4,6,8}
b = {1,2,3,4}

# x = a.union(b)
# print(x)
# # {1, 2, 3, 4, 6, 8}


# print(a.intersection(b))   # {2, 4} 

# print(a.difference(b))   #{8, 6}


# print(a.symmetric_difference(b))   #  {1, 3, 6, 8}


p = {23,45,76}
p1 = {4,6,5,7}
p.intersection_update(p1)
print(p)