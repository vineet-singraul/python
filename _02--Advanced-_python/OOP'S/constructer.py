class First:
    def __init__(self):
        print("Thise Is Constructer : ")
    def display(self):
        print("hello")
        print(id(self))
# obj = First
# obj.display()
obj = First()
obj.display()
print(id(obj))


