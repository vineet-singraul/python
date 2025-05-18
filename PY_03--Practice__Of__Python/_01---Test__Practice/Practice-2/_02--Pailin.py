# userinput = input("Enter String For Check Palindrome: ")
# length = len(userinput) 
# i = 0
# count = 0
# j = length - 1  

# while i < j: 
#     if userinput[i] != userinput[j]:
#         count = count + 1
#     i = i + 1
#     j = j - 1 
# if count == 0:  
#     print("User Input Is Palindrome Number :")
# else:
#     print("User Input Is Not The Palindrome Number :")



# or




userinput = input("Enter String For Check Palindrome: ")
res = userinput
p = userinput[::-1]

if(userinput == p):
    print("User Input Is Palindrome  :")
else:
    print("User Input Is Not Palindrome  :")

