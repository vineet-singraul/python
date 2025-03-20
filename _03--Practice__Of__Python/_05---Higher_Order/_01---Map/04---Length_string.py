# 4. **Use `map()` to find the length of each word in a given list of strings.**  
#    - **Input:** `["apple", "banana", "cherry"]`  
#    - **Output:** `[5, 6, 6]`  


# userInput = eval(input("Enter a itreations hare : ").split())
# ans = map(len , userInput)
# print(list(ans))



userInput = input("Enter words separated by spaces: ").split()
ans = map(lambda  x: len(x) , userInput)  
print(list(ans))  
