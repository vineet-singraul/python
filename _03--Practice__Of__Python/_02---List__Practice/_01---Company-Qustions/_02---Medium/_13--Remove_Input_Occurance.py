# 23. How do you remove all occurrences of a specific element from a list?

userInput = input("Enter a value want to remove : ")
li = [1,2,3,4,2,3,4,2,5,6,78]
for i in li:
    if i == int(userInput):
        li.remove(i)
print("After Removing element : ",li)