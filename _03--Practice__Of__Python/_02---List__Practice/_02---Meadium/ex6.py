# 17. **Find the index of a specific element**  
#     **List:** `my_list = ["apple", "banana", "cherry"]`  

#     **Output:**  
#     1  


li = ["apple", "banana", "mango"]
userInput = input("Enter A Name : ")

for i in li:
    if userInput == i:
        print(f' The User Input Is {userInput} and Index Is {li.index(i)}')