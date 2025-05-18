# 1. **Write a Python program using `map()` to find the square of each number in a given list.**  
#    - **Input:** `[1, 2, 3, 4, 5]`  
#    - **Output:** `[1, 4, 9, 16, 25]`  


li = eval(input("Enter a iterable for get sqare :"))

ans = map(lambda x: int(x)**2 , li)
print(list(ans))