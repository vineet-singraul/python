# // ### 2. **Ask the user for a key and check if its value is numeric.**  
# //    **User Input:**  
# //    Enter key to check: age  
# //    **Output:**  
# //    The value of 'age' is numeric.

Diction = {'name': 'vineet', 'age': '20', 'course': 'B-tech', 'Year': '4'}
userInput = input("Enter key to check: ")

if userInput in Diction:
   if Diction.get(userInput).isdigit():
      print("The value of ", userInput ,"is numeric")
   else:
      print("The value of ", userInput ,"is String")
