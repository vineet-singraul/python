# Example 10: Write a program to create a list from given string.


userInput = input("Enter The String : ")
i = 0
li = []
while i < len(userInput):
    li.append(userInput[i])
    print(userInput[i])
    i += 1
print(li)

