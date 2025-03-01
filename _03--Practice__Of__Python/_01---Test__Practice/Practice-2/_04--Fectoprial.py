# Write a program to find the factorial of a given number. 

userInpput = int(input("Enter A Number : "))
res = 1
for i in range(1 ,userInpput+1):
    res = res * int(i)
print("The Fectorial Of ",userInpput," Is : ",res)