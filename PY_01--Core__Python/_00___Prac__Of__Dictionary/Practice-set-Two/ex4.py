# 4. **Convert all dictionary values to uppercase if they are strings.**  
#    **Output:**  
#    Updated Dictionary: {'name': 'ALICE', 'city': 'NEW YORK'}


data = {'name': 'Vineet','city': 'satna'}
for key in data:
    val = data.get(key)
    data.update({key:val.upper()})
print("Finally Updated Dictionary : ",data)