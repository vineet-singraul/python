# x = 20
# def Update(p):
#     global x
#     x = p
#     print(x)

# print("Before Update Call:", x) 
# y = int(input("Enter Any Call: ")) 
# Update(y)  
# print("After Update Call:", y)









# for make the globle keys to local
x = 10
def Update(p):
    global x
    print("Before Update Call:", globals()['x']) 
    x = p
    print(x)

y = int(input("Enter Any Call: ")) 
print("Befor Updated : ",x)
Update(y)  
print("After Update Call:", x)
