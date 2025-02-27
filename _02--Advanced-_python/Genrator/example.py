# def first():
#     return "hello"

# x = first()
# print(x)




# def first():
#     yield "hello"

# x = first()
# print(x)



def first():
    yield 1
    yield 2
    yield 3

x = first()
print(x)
print(next(x))
print("hi")
print("hiiiii")
print("hello")
# print(list(x))