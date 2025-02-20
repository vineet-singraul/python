# 4. **Retrieve the value of a given key.**  
#    ```
#    Enter a key to retrieve value: age  
#    Value: 25
#    ```

diction = {"name":"vineet","age":20,"rollnum":1234}
userInput = input("Enter a key to retrieve value : ").lower()
print(userInput)
if userInput in diction.values() :
    print("Value:",userInput)
else :
    print("Value not exits")