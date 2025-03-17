class GrandFather:
    def Home(self):
        print("Thise Is Grand Father Home : ")

class Father(GrandFather):
    def Car(self):
        print("Thise Is Father Car : ")


class Child(Father):
    def Bike(self):
        print("Thise Is Child  Bike : ")

ob = Child()

ob.Home()
ob.Car()
ob.Bike()