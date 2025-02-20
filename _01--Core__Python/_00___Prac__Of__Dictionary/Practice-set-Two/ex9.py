# 13. **Ask the user to add a new key, but prevent duplicates.**  
#    **User Input:**  
#    Enter key: name  

#    **Output:**  
#    Key already exists! Try a different key.


data = {"name":"VIneet","Course":"B-Tech","City":"Satna","age":20,"Ending":2025}

userInput = input("Enter key: ")

if userInput in data.keys():
    print("Key already exists! Try a different key")
else:
    usreValue = input("Enter the Value: ")
    data[userInput] = usreValue
print("The Final Dictionary: ",data)