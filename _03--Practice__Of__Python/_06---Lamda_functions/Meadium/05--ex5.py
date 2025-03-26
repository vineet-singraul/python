# 15. **Find the GCD of Two Numbers**  
#     - Input: `12 18`  
#     - Output: `6`  

from functools import reduce

ui = [12, 18]
i = 2
n = min(ui)
li = []
while i <= n:
    ans = reduce(lambda x, y: i if x % i == 0 and y % i == 0 else None, ui)
    if(type(ans)==int):
        li.append(ans)
    i += 1 
print(f"Common divisor: {max(li)}")