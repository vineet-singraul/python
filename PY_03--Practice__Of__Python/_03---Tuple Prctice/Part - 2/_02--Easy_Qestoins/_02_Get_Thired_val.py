# 2. Access the third element of the tuple `(10, 20, 30, 40, 50)`.

# tu = (10, 20, 30, 40, 50)
# print(tu[2])



tu = (10, 20, 30, 40, 50)
i = 0
while (i < len(tu)-1):
    if i == 2:
        print(tu[i])
    i+=1
