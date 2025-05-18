# 23. **Find common elements between two lists**  
#     **List:** `list1 = [1, 2, 3, 4]`, `list2 = [3, 4, 5, 6]` 
#  
#     **Output:**  
#     [3, 4]  


li1 = [1, 2, 3, 4,6]
li2 = [3, 4, 5, 6]
li = []
for i in li1:
    for j in li2:
        if(i == j):
            li.append(j)
print(li)