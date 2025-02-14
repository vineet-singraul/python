# 12. **Remove all keys that contain numbers.**  
#    **User Input:**  
#    (No input required)  

#    **Output:**  
#    Updated Dictionary: {'name': 'Alice'}


data = {"name":"Vineet" , "Course":"B-Tech" , "Sem":"4" , "age":20}
newArr = {}
for key, val in data.items():
    if not (isinstance(val, int) or (isinstance(val, str) and val.isdigit())):
          newArr[key] = val
print(newArr)