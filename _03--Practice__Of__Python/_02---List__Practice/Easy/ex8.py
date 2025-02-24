# 8. **Sort a list in ascending order**  
#    **List:** `my_list = [5, 2, 8, 1]`  
#    **Output:**  
#    ```  
#    [1, 2, 5, 8]  
#    ```  





li = [5, 2, 8, 1]
x = sorted(li)
print(x)     #  return the new array 


            #  OR  #

li = [5, 2, 8, 1]
li.sort()  
print(li)    # change in real array :

            #  OR  #


li = [5, 2, 8, 1]
i = 0 
while i < len(li):
    j = 0
    while j < len(li):
        if li[i] > li[j]:
            li[i] , li[j] = li[j] , li[i]
        j += 1
    i += 1
print(li)