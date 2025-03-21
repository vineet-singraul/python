# ### 1. **Find the sum of all elements in a list**  
#    - **Input:** `[1, 2, 3, 4, 5]`  
#    - **Output:** `15` 

from functools import reduce
li = [1, 2, 3, 4, 5]

ans = reduce(lambda x,y : x+y , li)
print(ans)