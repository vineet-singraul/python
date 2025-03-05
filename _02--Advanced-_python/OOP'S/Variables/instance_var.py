# aise variable jo object badalne ke sath aapni value badel de INSTANCE VARIABLE KATE HAI 
# self ke sath jo variable hai vo instance variable hoga
# value se self ki kelp se hoga
# call karne ke liye object ke sath dot lagaker call  karte hai

# INTANCE VAR------>

# class Student:
#     def __init__(self,name,marks):
#         self.x = name
#         self.y = marks

#     def Show(self):
#         print(obj.x)
#         print(obj.y)


# obj = Student("Vineet" , 70)
# print(obj.x)
# print(obj.y)




# +++++++++  Class kE function ko call karo ++++++
# class Student:
#     def __init__(self,name,marks):
#         self.x = name
#         self.y = marks

#     def Show(self):
#         print(self.x)
#         print(self.y)


# obj = Student("Vineet" , 70)
# obj.Show()



# ++++++++++++++++++++++++++++++++++++++++++++++++






class Student:
    def __init__(self,name,marks):
        self.x = name
        self.y = marks

    def Show(self):
        print(self.x)
        print(self.y)


obj = Student("Vineet" , 70)
# call first object 
obj.Show()


# call second objescts
obj1 = Student("Mohni" , 70)
obj1.Show()
