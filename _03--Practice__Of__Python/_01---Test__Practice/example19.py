userInput = eval(input("Enter A Collection like (List , Tuple):"))
e = 0
o = 0
for i in userInput:
    if(i%2==0):
        e += 1
    else:
        o += 1
print("Number Of Even Number Is : ",e)
print("Number Of odd Number Is : ",o)