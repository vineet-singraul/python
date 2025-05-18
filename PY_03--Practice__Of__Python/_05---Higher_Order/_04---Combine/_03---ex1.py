# 2. **Filter Question:**  
#    Given a list of numbers `[10, 15, 20, 25, 30]`, use the `filter()` function to get only the numbers that 
#    are divisible by 5.


li = [10, 15, 20, 25, 39]
ans = filter(lambda x: x%5==0 , li)
print(list(ans))