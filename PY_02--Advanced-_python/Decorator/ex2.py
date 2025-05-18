def outer_fun(s):
    def inner_fun(p,q):
        p = p + 10
        q = q + 10
        r = s(p,q)
        print(r)
    return inner_fun
@outer_fun
def new(x,y):
    return x+y

p = 10
q = 20
new(p,q)