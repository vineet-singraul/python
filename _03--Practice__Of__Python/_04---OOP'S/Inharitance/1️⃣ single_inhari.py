class Animal:
    def Speeck(self): 
        print("Bark")

class Dog(Animal):
    def Eat(self):
        print("Bones")

ob = Animal()

ob1 = Dog()  
ob1.Eat() 
ob1.Speeck()  
