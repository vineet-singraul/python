# 3. **Check if a key exists in the dictionary.**  
#    ```
#    Enter a key to check: name  
#    Key exists: True
#    ```  


# diction = {"Name":"Vineet","Name":"Ajay","Name":"Ram","Name":"Mohni","Name":"MAhek"}
diction = {"Name":"Vineet","age":20,"RollNum":1234}
userInput = input("Enter a key to check : ")
if userInput in diction.keys() :
   print("key exiists : True")
else :
   print("key exiists : False")