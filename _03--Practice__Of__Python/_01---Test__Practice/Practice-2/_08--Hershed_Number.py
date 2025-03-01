# 9. Write a program to check given number is Harshad number/ Niven number or not. 10

userinput = input("Enter A Number : ")
res = 0
for i in userinput:
    res = res + int(i)

print(res)
if(res%int(userinput)==0):
    print("Number IS Harshad number/ Niven ")
else:
    print("Number IS Not Harshad number/ Niven ")
