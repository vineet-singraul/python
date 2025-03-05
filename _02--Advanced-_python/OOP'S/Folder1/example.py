class Student:
    def __init__(self):
        print("Constructor clled :")
    
    def __init__(self):
        print("Constructor clled 3 [OVERLOADDING]:")
    
obj = Student
# obj = Student()


# constructor ko baher se called ker sakte hai
obj.__init__()
