# Filter out words that are palindromes.  

# **Input:** `["madam", "hello", "racecar", "python", "level"]`  
# **Output:** `["madam", "racecar", "level"]`  


li = ["madam", "hello", "racecar", "python", "level"]
ans = filter(lambda x : x == x[::-1] , li)
print(list(ans))