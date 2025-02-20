#    Ask the user for a key and check if its value contains only alphabets.  
#    Enter key to check: name  
#    **Output:**  
#    The value of 'name' contains only alphabets.

data = {"name":"Vineet1" , "city":"Satna-jone-2" , "age":20}

userInput = input("Enter key to check:")
getValue = data.get(userInput)

for val in getValue:
    if val in '1234567890':
       print("The value of '",userInput,"' contains only alphabets")