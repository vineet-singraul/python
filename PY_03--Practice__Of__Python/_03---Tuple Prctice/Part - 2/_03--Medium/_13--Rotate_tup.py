# 23. Write a program to rotate the tuple `(1, 2, 3, 4, 5)` one step to the right.

# tu = (1, 2, 3, 4, 5)
# print(tu[::-1])



tu = (1, 2, 3, 0, 5)
for i in range(len(tu)-1, -1, -1):  
    print(tu[i])
