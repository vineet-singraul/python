# Filter names that start with the letter 'J'.  

# **Input:** `["John", "Alice", "James", "Michael", "Jessica"]`  
# **Output:** `["John", "James", "Jessica"]`  

li = ["John", "Alice", "James", "Michael", "Jessica"]
ans = filter(lambda x :'j' in x.lower() , li)
print(list(ans))