# li = 'vineet'
# si = "Singraul"
# print(li)
# print(si)
# li1 = frozenset(li)
# si1 = frozenset(si)
# print(li1)
# print(si1)

# c = li1.copy()
# print(c)


# 

# s = {10,20,30,40}
# x = frozenset(s)

# l = {100,200,30,40}
# y = frozenset(l)

# print(x.copy(y))

# print(x.union(y))

# print(x.difference(y))

# print(x.symmetric_difference(y))



#  +++++++++++++++++++++++++++++++++++++++++++++++++++
# a = x.isdisjoint(y)
# print(a)



s1 = {10,20,30,40}
x = frozenset(s1)

l1 = {10,20,30,40,34,56,78}
y = frozenset(l1)


print(y.issuperset(x))

print(x.issubset(y))