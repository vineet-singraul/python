# Filter out numbers that are divisible by both 3 and 5.  

# **Input:** `[10, 15, 30, 45, 50, 60]`  
# **Output:** `[15, 30, 45, 60]`  

li = [10, 15, 30, 45, 50, 60]
ans = filter(lambda x : x%3==0 and x%5==0  , li )
print(list(ans))