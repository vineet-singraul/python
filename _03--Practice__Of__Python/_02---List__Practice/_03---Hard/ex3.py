# 24. **Check if one list is a subset of another**  
#     **List:** `list1 = [1, 2, 3]`, `list2 = [1, 2, 3, 4, 5]`  


#     **Output:**  
#     True  

li1 = [1, 2, 3]
li2 = [1, 2, 3, 4, 5]
l = len(li1)
c=0
for i in li1:
    for j in li2:
        if i == j :
            f = True
            c = c +1
if(c == l):
    print("True")