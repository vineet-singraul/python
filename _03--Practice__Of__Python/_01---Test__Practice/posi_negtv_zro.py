# Example 3:Write a program to check given no is positive, negative or Zero.(Only if-elif-else
# statement)



def CheckNumber(userInput):
    if userInput > 0:
        print("The Number Given",userInput,"Is Positive :")
    elif userInput == 0:
        print("The Number Given",userInput,"Is Not A Positive Or Not A Negative :")
    else :
        print("The Number Given",userInput,"Is Negative :")
        
        
userInput = eval(input("Enter A Number : "))
CheckNumber(userInput)
