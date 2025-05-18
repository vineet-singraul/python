

# output element is always equal to one element
# output me only single element return aayega


# x = [12,3,4,5,6,7,8,9]
# y = x.map() 


def sqr(n):
    return n**2

li = [12,3,4,5,6,7,8,9]
x = map(sqr , li)

print(x)
print(list(x))
