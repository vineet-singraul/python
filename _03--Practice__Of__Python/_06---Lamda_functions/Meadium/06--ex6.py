# 17. **Remove Duplicates from a List**  
#     - Input: `[1, 2, 2, 3, 4, 4, 5]`  
#     - Output: `[1, 2, 3, 4, 5]` 

li = [1, 2, 2, 3, 4, 4, 5]
ans = lambda x : set(x)
print(ans(li))