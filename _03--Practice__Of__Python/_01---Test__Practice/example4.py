# Write a program to swap two variables without using third variable.

def swap(userInput1,userInput2):
    temp = userInput1
    userInput1 = userInput2
    userInput2 = temp
    print("------ After Perform Swapping ------")
    print("userInput1 Value Is : ",userInput1)
    print("userInput2 Value Is : ",userInput2)
     



userInput1 = eval(input("Enter The First Number: "))
userInput2 = eval(input("Enter The Second Number: "))
print("------ Befor Perform Swapping ------")
print("userInput1 Value Is : ",userInput1)
print("userInput2 Value Is : ",userInput2)
swap(userInput1,userInput2)