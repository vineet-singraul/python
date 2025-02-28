# 3. **Count occurrences of an element in a tuple**  
#    **Input:**  
#    Enter a tuple: (1, 2, 3, 2, 4, 5, 2, 6)  
#    Enter the number to count: 2  

#    **Output:**  
#    3  

# tu = tuple(input("Enter The Tuple Elements : "))
# s = len(tu)
# i = 0
# count = 0
# Select = int(input("Enter Number You Want TO Count : "))

# while Select < s:
#     j = i +1
#     while j < s:
#         if Select == tu[j]:
#           count = count + 1
#         j+=1
#         print("hi")
#     i+=1
#     print("hxxxxxi")
#     break
# print("Number Of Occurance Of ",Select," Is : ",count)
# (1,2,3,2,4,5,2,6)






tu = tuple(input("Enter The Tuple Elements : ").split())
count = 0
Select = int(input("Enter Number You Want TO Count : "))

for i in tu:
    if Select == int(i):
        print(i)
        count = count + 1
print("Number Of Occurance Of ",Select," Is : ",count)