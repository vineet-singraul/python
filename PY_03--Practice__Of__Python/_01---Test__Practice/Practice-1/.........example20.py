# userInput = int(input("Enter A Number :"))
# count = 0 

# for i in range(1, userInput + 1): 
#     if userInput % i == 0:
#         count += 1

# if count == 2:
#     print(userInput, "is a Prime Number")
# else:
#     print(userInput, "is NOT a Prime Number")








userInput = int(input("Enter A Number :"))
count = 0 

for i in range(1, userInput + 1): 
    if userInput % i == 0:
        count += 1
    if count == 2:
        print(i , end=",")
    