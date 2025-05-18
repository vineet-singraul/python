# 3. **Reduce Question:**  
#    Given a list `[1, 2, 3, 4, 5]`, use the `reduce()` function from `functools` to find the product of all 
#     numbers in the list.

from functools import reduce
li = [ 2, 3, 4]
ans  = reduce(lambda x,y : x*y , li)
print(ans)