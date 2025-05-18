# Filter out even numbers from a given list of numbers.  

# **Input:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
# **Output:** `[2, 4, 6, 8, 10]`  


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = filter(lambda x : x if x%2==0 else x , li)
print(list(ans))