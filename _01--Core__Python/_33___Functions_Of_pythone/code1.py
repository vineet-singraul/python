def AddNumnber(x,y,z):
    "for addtion of 3 variable "
    return x+y+z

p = int(input("Enter One : "))
q = int(input("Enter Two : "))
r = int(input("Enter Three : "))

res = AddNumnber(p,q,r)
print(res)
print(AddNumnber.__doc__)