# 15. **Replace a specific value in a list**  
#     **List:** `my_list = [10, 20, 30, 40]`  

#     **Output:**  
#     [10, 25, 30, 40]  

# li =  [10, 20, 30, 40]
# useInput = eval(input("Enter You Want To add :"))
# print(li + useInput)


#      OR         #


li =  [10, 20, 30, 40]
useInput = eval(input("Enter You Want To add :"))
li.append(useInput)
print(li)