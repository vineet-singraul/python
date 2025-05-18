# 32. Write a function to check if a tuple is sorted in ascending order.

# userInput = tuple(map(int, input("Enter a tuple of numbers: ").split()))
# n = userInput[1]
# print(n)
# for i in userInput:
#     for j in range(n , len(userInput)):
#         if i>j:
#             f = True
#         else:
#             f = False
# if f == True:
#     print("Thise Is Accending orderred all element : ")
# else:
#     print("Thise Is not Accending orderred all element : ")















userInput = tuple(map(int, input("Enter a tuple of numbers: ").split()))
f = True  

for i in range(len(userInput) - 1): 
    if userInput[i] > userInput[i + 1]:  
        f = False  
        break 

if f:
    print("Yes, it's in ascending order.")
else:
    print("No, it's not in ascending order.")
