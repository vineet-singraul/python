# 13. **Count occurrences of an element in a list**  
#     **List:** `my_list = [1, 2, 2, 3, 2, 4, 5]`  

#     **Output:**  
#     3  


li = [1, 2, 2, 3, 2, 4, 5]
i = 0
count = 0
while i < len(li):
    j = i+1
    while j < len(li):
        if li[i] == li[j]:
            count = count + 1
        j+=1
    i+=1
print(count)