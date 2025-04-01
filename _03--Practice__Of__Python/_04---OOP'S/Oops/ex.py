class Parent:
    roll = 23
    def show(self):
        print("Parent")

class Child(Parent):
    def show1(self):
        print("child")

        


ob = Child()
ob.show()
