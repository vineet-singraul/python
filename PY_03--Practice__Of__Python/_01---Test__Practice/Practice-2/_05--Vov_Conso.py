# 5. Write a program to find how many vowels and consonants are present in strings. 

userInput = input("Enter A String :")
vovels = ('A','E','I','O','U','a','e','i','o','u')
v = 0
c = 0
for i in userInput:
    if i in vovels:
        v = v + 1
    else:
        c = c + 1
print("The Number of vowels in string :",v )
print("The Number of consonants in string :",c )