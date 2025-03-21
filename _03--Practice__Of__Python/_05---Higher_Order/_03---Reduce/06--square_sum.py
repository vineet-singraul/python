# ### 8. **Find the sum of squares of elements in a list**  
#    - **Input:** `[1, 2, 3]`  
#    - **Output:** `14` (since `1^2 + 2^2 + 3^2 = 14`)  

from functools import reduce
li = [1, 2, 3]
ans = reduce(lambda x,y : x+(y**2),li)
print(ans)