# parant chiled relationship called inharitance 

# single laval.-->
    
 
class A:
    x = 10
    def home(self):
        print("Home Page c:")

class B(A):
    def Car(self):
        print("Car Page : ")


obj = B()
print(obj.x)
obj.Car()
obj.home()