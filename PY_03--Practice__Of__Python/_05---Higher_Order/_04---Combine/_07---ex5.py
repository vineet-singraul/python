# 5. **Reduce with a Custom Function Question:**  
#    Given a list `[100, 50, 25, 5]`, use `reduce()` to perform a subtraction operation from left to right.

from functools import reduce
li = [100, 50, 25, 5]
ans  = reduce(lambda x,y : x-y , li)
print(ans)