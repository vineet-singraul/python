# 17. How do you copy a list without modifying the original?

# li = [1,2,3,4,5]
# print(id(li))
# l2 = []
# l2.copy()
# print(id(li))


# ---------------------------


li = [1,2,3,4,5]
li2 = []
for i in li:
    li2.append(i)
print(li2)