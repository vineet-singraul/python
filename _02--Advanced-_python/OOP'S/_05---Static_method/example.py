class Book:
    def __init__(self):
        print("Constructer Cales ")
    
    @staticmethod
    def Welcome():
       print("Welocme : ")

    @staticmethod
    def Thanks():
            print("Thnkas")
        
obj = Book()
Book.Welcome()
Book.Thanks()