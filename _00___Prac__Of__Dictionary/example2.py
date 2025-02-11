# Ask the user to add another key-value pair.

# Enter another key: age  
# Enter another value: 25  
# Updated Dictionary: {'name': 'Alice', 'age': '25'}

dictio = {}
i = 0
while i<2:
  userKeys =  input("Enter Keys : ")
  userValue = input("Enter Value : ")
  dictio.update({userKeys:userValue})
  i+=1
print("Dictionary Is : ",dictio)