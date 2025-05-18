# Write a program to get the Fibonacci series

num = int(input("Enter Number You Want To Print Seriese : "))

a,b = 0,1
print("Fibbo  Series Is : " , end=' ')
for i in range(num):
    print(a , end=' ')
    a,b = b, a+b