# def add (*n):
#     print(n)
#     print(type(n))
#     sum = 0
#     for i in n:
#         sum = sum + i
#     return sum
# res = add(2,3,4,5,6)
# print(res)


# dynamic input

# def add (*n):
#     print(n)
#     print(type(n))
#     sum = 0
#     for i in n:
#        for j in i:
#         sum = sum + j
#     return sum

# x = eval(input("Enter One Number:"))
# res = add(x)
# print(res)


def add (*n):
    print(n)
    print(type(n))
    sum = 0
    for i in n:
       for j in i:
        sum = sum + j
    return sum

x = eval(input("Enter One Number:"))
res = add(x)
print(res)