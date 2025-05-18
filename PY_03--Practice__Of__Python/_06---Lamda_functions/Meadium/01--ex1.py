# 11. **Find the Second Largest Number in an Array**  
#     - Input: `[1, 5, 3, 8, 7]`  
#     - Output: `7`  

li = [1, 5, 3, 8, 7]
l = max(li)  
li.remove(l)  
ans = lambda x: max(x) if x else "Not Max : " 
print(ans(li))


