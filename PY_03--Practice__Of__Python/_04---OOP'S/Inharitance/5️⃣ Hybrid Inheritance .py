class A:
    def __init__(self, name):
        print("Class A Constructor :")
        self.name = name
    def Show(self):
        print("Class A Name Is : ",self.name)

class B(A):
    def __init__(self, name):
        print("Class B Constructor : ")
        self.name = name
    def Show(self):
        print("Class B Name Is :",self.name)

class C(A):
    def __init__(self, name):
        print("Class C Constructor : ")
        self.name = name
    def Show(self):
        print("Class C Name Is :",self.name)


class D(B,C):
    def __init__(self, name):
        print("Class D Constructor : ")
        self.name = name
    def Show(self):
        B.Show(self)
        print("Class D Name Is :",self.name)

ob = D("Vineet")
ob.Show()
