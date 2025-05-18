# 12. **Find the maximum and minimum values in a list**  
#     **List:** `li = [10, 5, 20, 8]`


#     **Output:**  
#     20 5  


# +++++++++++++++++++++++++++++++++++

# li = [10, 5, 20, 8]
# print(min(li))
# print(max(li))

# +++++++++++++++++++++++++++++++++++


# li = [10, 5, 20, 8]
# i = 0 
# while i < len(li):
#     j = i+1
#     while j < len(li):
#         if li[i] > li[j]:
#             m = li[i]
#             break
#         else:
#             m = li[j]
#             break
#         j += 1
#     i+=1
# print(m)


# +++++++++++++++++++++++++++++++++++


# li = [2, 10, 20, 12, 10]
# i = 0
# n = m = 0

# while i < len(li) - 1:  
#     if li[i] > li[i+1]:
#         m = li[i]
#     else:
#         m = li[i+1]
#     i = i + 1
    
#     if n < m:
#         n = m

# print(n)  




# +++++++++++++++++++++++++++++++++++


li = [10,200,300,2,3,4,6]
n = li[0]

for i in li:
    if i>n:
        n = i
print(n)