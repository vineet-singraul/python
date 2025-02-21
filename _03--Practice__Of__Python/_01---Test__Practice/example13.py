# Write a program to find factorial of given no.


def FectorialFind(userInput):
    i = 1
    fec = 1
    while(i<=userInput):
        fec = fec * i
        i = i + 1
    print("The Fectorial Of ",userInput," Is = ",fec)
userInput = int(input("Enter A Number You Want To Find A Fectorial : "))
FectorialFind(userInput)