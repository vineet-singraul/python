# ### 10. **Find the difference between cumulative sums in a list**  
#    - **Input:** `[10, 5, 2]`  
#    - **Output:** `3` (since `10 - 5 - 2 = 3`)  

from functools import reduce
li = [10 , 5 , 2]
ans = reduce(lambda x,y : x-y , li)
print(ans)