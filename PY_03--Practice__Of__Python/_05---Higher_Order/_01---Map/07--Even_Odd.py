# 8. **Use `map()` to determine whether each number in a list is even or odd, returning "Even" or "Odd".**  
#    - **Input:** `[1, 2, 3, 4, 5]`  
#    - **Output:** `["Odd", "Even", "Odd", "Even", "Odd"]`  

li = [1,2,3,4,5]
ans = map(lambda x : "Evan" if x%2==0 else "Odd" , li)
print(list(ans))