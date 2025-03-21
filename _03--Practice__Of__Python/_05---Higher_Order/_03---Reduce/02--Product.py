# ### 2. **Find the product of all elements in a list**  
#    - **Input:** `[2, 3, 4]`  
#    - **Output:** `24`


from functools import reduce
li = [2, 3, 4]

ans = reduce(lambda x,y : x*y , li)
print(ans)