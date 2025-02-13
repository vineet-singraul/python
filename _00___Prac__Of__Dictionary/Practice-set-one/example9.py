# 9. **Show all key-value pairs.**  
#    ```
#    name: Alice  
#    city: New York  
#    country: USA  
#    ```  

diction = {"Name": "Vineet", "age": 20, "RollNum": 1234}

for key, val in diction.items():
    print(f"{key}: {val}")
