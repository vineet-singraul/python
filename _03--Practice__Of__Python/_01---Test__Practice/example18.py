userInput = (input("Enter A Number :"))
sum = 0
for i in userInput:
    i = int(i)
    sum = sum + (i**3)
if str(sum) == userInput:
    print("You Entered ",userInput," and It Is Armstrong Number")
else:
    print("You Entered ",userInput," and It Is Not Armstrong Number")