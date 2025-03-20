# 2. **Use `map()` to convert a list of lowercase strings into uppercase.**  
#    - **Input:** `["hello", "world", "python"]`  
#    - **Output:** `["HELLO", "WORLD", "PYTHON"]`  


# userInput = input("Enter something for convert upper case word : ").split(' ')
# def upperConvertor(x):
#     return x.upper()

# ans = map(upperConvertor , userInput)
# print("Upper Correction Is : ",list(ans))



# ------Lamda---------




userInput = input("Enter something for convert upper case word : ").split(' ')
ans = map(lambda x:x.upper() , userInput)
print(list(ans))