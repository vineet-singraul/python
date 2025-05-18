# 21. **Find the second largest element in a list**  
#     **List:** `my_list = [10, 20, 4, 45, 99]`  

#     **Output:**  
#     45  


li = [10, 20, 4, 45, 99,98]

n = li[0]

for i in li:
    if i > n :
        n = i

for i in li :
    if n > i:
        m = i
print("Second Max Value Is : ",m)