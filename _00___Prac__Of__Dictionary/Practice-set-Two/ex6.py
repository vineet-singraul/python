# 7. **Ask the user for a key and append its value to a list.**  
#    **User Input:**  
#    Enter key to append value: age  

#    **Output:**  
#    Value list: [25]


data = {"age": 20, "name": "Vineet", "city": "satna"}
li = []
userinput = input("Enter key to append value: ")
getValue = data.get(userinput)
li.append(getValue)
print(li)