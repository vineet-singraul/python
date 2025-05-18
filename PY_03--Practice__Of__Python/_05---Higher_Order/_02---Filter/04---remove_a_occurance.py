# ### **Question 4:**  
# Filter out strings that contain the letter 'a' from a given list.  

# **Input:** `["dog", "cat", "rabbit", "lion", "tiger"]`  
# **Output:** `["dog", "lion", "tiger"]`  

uI = ["dog", "cat", "rabbit", "lion", "tiger"]
ans = filter(lambda x :'a'not in x , uI)
print(list(ans))