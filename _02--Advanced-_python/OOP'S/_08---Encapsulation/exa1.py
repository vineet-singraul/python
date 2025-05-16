class Emp:
    def __init__(self,age):
        self.__age = age
    
    def show(self):
        print("User Age Is : ",self.__age)
    
ob = Emp(21)
ob.show()
ob.show()
print(ob._Emp__age)
print(ob._Emp__age)