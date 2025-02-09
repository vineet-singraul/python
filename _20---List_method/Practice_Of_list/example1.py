li = [10,20,30,40,50 , [10,29,43,45]]
li2 = [10,20,30,40,50]

print(li)   # [10, 20, 30, 40, 50]  -->  Orderd

print(li[3])  # 40  ---> gatting by index

print(id(li))   #  1950492973312
print(id(li2))    #  1950492971392 -----> Mutable


strlist = ["Vineet", "Ajay", "riya", "Priya"]
print(strlist[:])   
print(strlist[1:3])   

lists = [1,2,3,4,5,6,7,8]
print(lists[-1:-4:-2])    # [8, 6]
print(lists[-1:5:-1])     # [8, 7]
print(lists[-3:-1:1])     # [6, 7]
print(lists[0:-1:-1])    #[]
print(lists[0:-1:1])    # [1,2,3,4,5,6,7,8]
print(lists[::-1])    # [8, 7, 6, 5, 4, 3, 2, 1]




