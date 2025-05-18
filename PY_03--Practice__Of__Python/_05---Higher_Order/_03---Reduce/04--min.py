# ### 3. **Find the maximum value in a list**  
#    - **Input:** `[10, 25, 5, 30, 15]`  
#    - **Output:** `30`  

from functools import reduce
li = [10, 25, 5, 30, 15]
ans  = reduce(lambda x,y : x if x<y else y ,li)
print(ans)