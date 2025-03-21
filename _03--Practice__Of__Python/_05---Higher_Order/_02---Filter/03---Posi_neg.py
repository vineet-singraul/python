# ### **Question 3:**  
# Filter only positive numbers from a list of integers.  

# **Input:** `[-5, -3, 0, 2, 4, -1, 6]`  
# **Output:** `[2, 4, 6]`  


# ui = list(input("Enter a itreations: ").split(','))
# ans = filter(lambda x : int(x)<0 , ui)
# print(list(ans))


ui = list(input("Enter a itreations: ").split(','))
ans = filter(lambda x: int(x) < 0, ui) 
print(list(ans))
