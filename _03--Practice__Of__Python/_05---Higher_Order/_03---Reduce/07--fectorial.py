# ### 9. **Compute the factorial of a number using a list**  
#    - **Input:** `[1, 2, 3, 4, 5]`  
#    - **Output:** `120` (since `1 × 2 × 3 × 4 × 5 = 120`)  

from functools import reduce
li = [1,2,3,4,5]
ans  = reduce(lambda x,y : x*y , li)
print(ans)