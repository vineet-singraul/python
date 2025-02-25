# 14. **Insert an element at a specific index**  
#     **List:** `my_list = [1, 2, 4, 5]`  

#     **Output:**  
#     [1, 2, 3, 4, 5]  


li =  [1, 2, 3, 4, 5]  
i = 0 
while i < len(li)-1:
    if li[i] + 1 ==  li[i+1]:
        pass
    else:
        li[i+1] = li[i]+1
    i+=1
print(li)


