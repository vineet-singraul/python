# 15. How do you count the occurrences of an element in a list?

li = [1,2,3,4,43,2,1,4,1,3,2]

userInput = int(input("Enter A Value For Find Occurance : "))
count = 0
for i in li :
    if i == userInput:
        count = count + 1
print("The Entered Is ",userInput," And That Occurance Is :",count)