# 20. Convert the tuple `(1, 2, 3, 4, 5)` into a dictionary with keys as elements and values as their squares.

tu = (1, 2, 3, 4, 5)
dic = {}
for i in tu:
    dic[i] = i*i
print(dic)