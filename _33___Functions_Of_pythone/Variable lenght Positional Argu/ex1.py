def add (*n):
    print(n)
    print(type(n))
    sum = 0
    for i in n:
        sum = sum + i
    return sum
res = add(2,3,4,5,6)
print(res)