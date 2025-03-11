# 11. Merge two tuples `(1, 2, 3)` and `(4, 5, 6)`.

# solve - 1:
# li1 = (1,2,3)
# li2 = (4,5,6)
# li1 = li1 + li2
# print(li1)




# solve - 2 
li1 = (1,2,3)
li2 = (4,5,6)
li3 = []

for i,j in zip(li1,li2):
    li3.append(i)
    li3.append(j)
print(tuple(li3))



