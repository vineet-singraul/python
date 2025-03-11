# class A:
#     def home(self):
#         print("Class A")

# class B(A):
#     def Car(self):
#         print("Class B")

# class C(B):
#     def Car(self):
#         super().Car()
#         print("Class C")


# obj = C()
# obj.home()
# obj.Car()







class A:
    def Car(self):
        print("Class A")

class B(A):
    def Car(self):
        print("Class B")

class C(B):
    def Car(self):
        super(B, self).Car()  
        print("Class C")

obj = C()
obj.Car()
