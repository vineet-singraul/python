# Example 2: Write a program to calculate the sum of numbersdef

def SumOfNumbers(userInput):
    i = 0
    sum = 0
    while(i<=userInput):
        sum = sum + i
        i = i + 1
    print("The Sum Of Number 1 to ",userInput," = ",sum)
userInput = int(input("Enter a number Want to sum :"))
SumOfNumbers(userInput)