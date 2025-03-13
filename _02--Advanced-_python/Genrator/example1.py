





# def first():
#     return "hello"

# x = first()
# print(x)





# genratoe -----> key word hai


# def first():
#     yield "hello"

# x = first()
# print(x)



# def first():
#     yield 10
#     yield 2
#     yield 3

# x = first()
# print(x)
# print(next(x))
# print("hi")
# print("hiiiii")
# print("hello")
# print(next(x))

# print(next(x))

# print(list(x))
















def natralNum(x):
    i=1
    while i<=x:
        yield i
        i = i + 1

n = 10
p = natralNum(10)

print(next(p))
for i in p:
    print(i)
    print("vineet")





