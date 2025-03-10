# 3. Extract the last three elements from the tuple `(1, 2, 3, 4, 5, 6)`.

tu = (1, 2, 3, 4, 5, 6,3 ,5,7)
l = len(tu)
for i in range(l-3, l):
    print(tu[i])
