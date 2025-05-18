from functools import reduce

li = [20,2,3,4,5,6,7,8,9]

def MyMax(x,y):
    if(x>=y):
        return x
    else:
        return y
p = reduce(MyMax ,li)
print(p)