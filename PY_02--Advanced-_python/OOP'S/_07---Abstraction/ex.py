# from abc import ABC, abstractmethod 

# class A(ABC):
#     def new(self):
#         print("80%")

#     @abstractmethod
#     def new1(self):
#         pass

#     class B(A):
#         def new1(self):
#             print("20%")

#     obj = B()
#     obj.new1()






















from abc import ABC, abstractmethod 

class A(ABC):
    def new(self):
        print("80%")

    @abstractmethod
    def new1(self):
        pass

class B(A):
    def new1(self):
        print("20%")

obj = B()
obj.new1()
