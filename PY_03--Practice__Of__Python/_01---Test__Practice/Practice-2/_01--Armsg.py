# 1. Write a program to check if a given number is an Armstrong number.


res = 0
userInput = input("Enter Any one Number :")
leng = len(userInput)

for i in userInput:
    res = res + int(i)**leng

if int(userInput) == res:
    print(userInput," of Armstrong Is : ",res)
else:
    print(userInput," Is Not A Armstrong : ",res)
