# 6. **Convert a list of numeric strings into a list of integers using `map()`.**  
#    - **Input:** `["10", "20", "30"]`  
#    - **Output:** `[10, 20, 30]`  

ui = ["10" , "20" , "30"]
ans = map(lambda x: int(x) , ui)
print(list(ans))