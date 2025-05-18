# ### 5. **Concatenate a list of strings**  
#    - **Input:** `["Hello", " ", "World", "!"]`  
#    - **Output:** `"Hello World!"`  

from functools import reduce
li = ["Hello", " ", "World", "!"]
ans = reduce(lambda x , y : x+y , li)
# ans = reduce(lambda x , y : str(x)+str(y) , li)
print(ans)