# Slicing With String
name = "Vineet Kaise ho"
print(name[::-1])
print(name[-1:3:-1])
print(name[-1:-3:-1])
print(name[1:3:-1])
print(name[1:-3:1])
print(name[1:-3:-1])
print(name[-1:-3:1])


# String With Concatinate opreator
name1 = "Vineet"
name2 = "Singh"
x = 10
# print(name+x)   # errpr Type -- string only cancinate
print(name1+name2)



# Strig With copyies operator
print(name1*2)     #VineetVineet
print(10*name1)   #VineetVineetVineetVineetVineetVineetVineetVineetVineetVineet


#  doble start  operatior **
# print(name2**2)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'



city = "Bhopal Is the best place to visite in madhya pradesh of india"
print("Bhopal" in city)
print("bhopal" in city)


city1 = "a e i o u A E I O U"
ch = city1
for ch in city1:
    print(ch)