# 6. **Add multiple key-value pairs.**  
#    ```
#    How many key-value pairs do you want to add? 2  
#    Enter key: city  
#    Enter value: New York  
#    Enter key: country  
#    Enter value: USA  
#    Final Dictionary: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}


dictionary = {}
userCount = int(input("How many key-value pairs do you want to add ? "))
i = 0
while i < userCount:
    userInput = input("Enter key : ") 
    userValue = input("Enter Value : ")
    dictionary.update({userInput:userValue})
    i = i + 1
print("Final Dictionary : ",dictionary)