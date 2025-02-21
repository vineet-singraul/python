







# Example 3: Write a program to find odd no. (2,4,6,8,….)

# def CheckEven():
#     i = 1
#     while(i<=userInput):
#         print(2*i-1,end=",")
#         i = i + 1



# userInput = int(input("Enter A Number "))
# CheckEven()/





def CheckEven(userInput):
    i = 1
    while(i<=userInput):
        if(i%2==0):
            print(i)
        i += 1
userInput = int(input("Enter A Number "))
CheckEven(userInput)