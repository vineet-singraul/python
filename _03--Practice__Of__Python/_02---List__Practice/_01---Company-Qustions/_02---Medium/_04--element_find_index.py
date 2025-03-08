# 14. How do you find the index of an element in a list?

li = [1,2,3,4,5,6,7,8,9]
userInput = int(input("Enter Value You Want To Find  : "))

for i in li:
    if i == userInput:
        print("The value Is ",userInput,"and Index Is : ",li.index(userInput))