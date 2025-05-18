# 7. **Find the Sum of Digits**  
#    - Input: `123`  
#    - Output: `6`  


# i = 123
# ans = lambda x : sum(int(x) for x in str(i))
# print(ans(i))

from functools import reduce
i = 123
li = list(str(i))
print(li)
ans = reduce( lambda x,y: int(x) + int(y) , li)
print(ans)