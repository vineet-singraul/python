# class A:
#     x = 10
#     def home(self):
#         print("Class A")

# class B():
#     def Car(self):
#         print("Class B")

# class C(A,B):
#     def bank(self):
#         print("Class C")


# obj = C()
# print(obj.x)
# obj.home()
# obj.Car()
# obj.bank()




# method resolution order se object decide karta hai ki kon fun pahle calega












class A:
    def home(self):
        print("Class A")

class B(A):
    def home(self):
        super().home()
        print("Class B")

obj = B()
obj.home()

# parant class ki method dairect acssess ker sakte gai super method se 
