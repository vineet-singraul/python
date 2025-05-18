# ### 7. **Find the longest word in a list**  
#    - **Input:** `["apple", "banana", "cherry", "blueberry"]`  
#    - **Output:** `"blueberry"` 

from functools import reduce
li = ["apple", "banana", "cherry", "blueberry"]
ans = reduce(lambda x,y : x if len(x)>len(y) else y , li)
print(ans)
