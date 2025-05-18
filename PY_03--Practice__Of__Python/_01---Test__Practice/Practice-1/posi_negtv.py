# Example 2:Write a program to check given no is positive or negative. (Only if-else statement)


def CheckNumber(userInput):
    if userInput > 0:
        print("The Number Given",userInput,"Is Positive :")
    else :
        print("The Number Given",userInput,"Is Negative :")
        
        
userInput = eval(input("Enter A Number : "))
CheckNumber(userInput)
