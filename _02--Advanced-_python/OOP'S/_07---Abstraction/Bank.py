from abc import ABC, abstractmethod 

class Bank(ABC):
    def resister(self):
        print("Resister Page :")
    
    def logout(self):
        print("logout Page :")

    @abstractmethod
    def authentication(self):
        pass
    def dashBoard(self):
        print("From DashBoard")

class WebPage(Bank):
    def login(self,id,passw):
         self.id = id
         self.passw = passw
    def show(self):
        print("ID : ",self.id)
        print("PASS : ",self.passw)

    def authentication(self):
        print("Authentication Done")

obj = WebPage()
obj.dashBoard()
obj.show()
obj.login(100 , 123)
