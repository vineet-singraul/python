# Example 6:Write a program to swap two variables using using Addition and Subtraction

def swapVariables(numberone, numbersecond):
    print("After Performe The Swapping")
    numberone = numberone + numbersecond
    numbersecond = numberone - numbersecond
    numberone = numberone - numbersecond
    print("After Performe The Swapping")
    print("UserInputone Value one = ",numberone)
    print("UserInputsecond Value one = ",numbersecond)


numberone = int(input("Enter The First Value : "))
numbersecond = int(input("Enter The First Value : "))
print("Befor Performe The Swapping")
print("UserInputone Value one = ",numberone)
print("UserInputsecond Value one = ",numbersecond)
swapVariables(numberone, numbersecond)