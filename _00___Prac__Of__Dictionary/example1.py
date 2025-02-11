# Create a dictionary with a key-value pair entered by the user.

# Enter key: name  
# Enter value: Alice  
# Dictionary: {'name': 'Alice'}

dict = {}
userInput = input("Enter key : ")
userValue = input("Enter value : ")
dict.update({userInput:userValue})
print("Dictionary: ",dict)