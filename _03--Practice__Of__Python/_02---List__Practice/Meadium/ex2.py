# 12. **Find the maximum and minimum values in a list**  
#     **List:** `li = [10, 5, 20, 8]`


#     **Output:**  
#     20 5  


# +++++++++++++++++++++++++++++++++++

# li = [10, 5, 20, 8]
# print(min(li))
# print(max(li))

# +++++++++++++++++++++++++++++++++++


li = [10, 5, 20, 8]
i = 0 
while i < len(li):
    j = i+1
    while j < len(li):
        if li[i] > li[j]:
            m = li[i]
            break
        else:
            m = li[j]
            break
        j += 1
    i+=1
print(m)