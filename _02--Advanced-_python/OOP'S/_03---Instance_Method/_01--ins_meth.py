# class Student:
#     def first(self):
#         print("Thise Is Form First : ")
    
#     def second(self):
#         Student.first(self)

# obj = Student()
# obj.first()
# obj.second()




#  ----------------------------------------



class Student:
    def first(self):
        print("Thise Is Form First : ")
    
    def second(self):
        obj1 = Student()
        obj1.first()

obj = Student()
obj.first()
obj.second()