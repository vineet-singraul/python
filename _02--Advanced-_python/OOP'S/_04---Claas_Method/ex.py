class Book:
    price = 100
    pages = 500

    def __init__(self , name):
        self.x = name
        print("Name : " , self.x)
        print("Price : ",Book.price)
        print("Pages : ",Book.pages)

    @classmethod
    def Update(cls , p ,q):
        cls.price = p
        cls.pages = q

Book.Update(200 , 1200)
obj1 = Book("Vineet")
print("--------------")
obj2 = Book("Anmol")


