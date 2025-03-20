# 3. **Convert a list of temperatures from Celsius to Fahrenheit using `map()`.**  
#    - **Input:** `[0, 20, 30, 40]`  
#    - **Output:** `[32.0, 68.0, 86.0, 104.0]`  

userInput = list(input("Enter a temperatures : ").split())
ans = map(lambda x: ((9/5) * int(x)) + 32, userInput)
print(list(ans))