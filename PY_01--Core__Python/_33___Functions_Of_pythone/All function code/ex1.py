# def add(x,*n,y=0,**m):
#     print(x)
#     print(y)
#     print(n)
#     print(m)

# add(10,20,30,40,50,y=100,z=10,p=2,q=4)



# def add(x,y=20):
# # def add(y=20,x):
#     print(x)
#     print(y)
# add(10,20)




# def add(x,*n):
# # def add(y=20,x):
#     print(x)
#     print(n)
# add(10,20,30,40,0)





def add(*n,**m):
    print(n)
    print(m)

add(10,20,30,40,50,y=100,z=10,p=2,q=4)