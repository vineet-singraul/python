# Filter out words from a list that have more than 5 letters.  

# **Input:** `["apple", "banana", "grape", "kiwi", "mango"]`  
# **Output:** `["apple", "grape", "kiwi"]`  

# ui = ["apple", "banana", "grape", "kiwi", "mango"]

ui = list(input("Enter Something: ").split(','))
ans = filter(lambda x : len(x)<=5 , ui)
print(list(ans))