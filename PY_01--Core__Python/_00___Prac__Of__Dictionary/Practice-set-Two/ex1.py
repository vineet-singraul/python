# 1. **Ask the user to create a dictionary by entering key-value pairs until they type 'stop'.**  
#    **User Input:**  
#    ```
#    Enter key: name  
#    Enter value: Alice  
#    Enter key: age  
#    Enter value: 25  
#    Enter key: stop  
#    ```  
#    **Output:**  
#    ```
#    Final Dictionary: {'name': 'Alice', 'age': '25'}
#    ```


dictioan = {}

while True:
    keyinput = input("Enter key: ")
    if keyinput == 'stop':  
        break  

    Valueinput = input("Enter value: ")
    dictioan.update({keyinput:Valueinput})

print("Final Dictionary:", dictioan)
