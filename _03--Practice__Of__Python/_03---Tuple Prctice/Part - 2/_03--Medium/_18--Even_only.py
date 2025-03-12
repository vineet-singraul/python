# 28. Extract only even numbers from `(1, 2, 3, 4, 5, 6, 7, 8)`.

tu = (1, 2, 3, 4, 5, 6, 7, 8)
li = []
for i in tu:
    if (i%2==0):
       li.append(i)
tu = tuple(li)
print(tu)