# 7. Count how many times `2` appears in the tuple `(1, 2, 3, 2, 4, 2, 5)`.

tu = (1, 2, 3, 2, 4, 2, 5)
userInput = int(input("Enter Want To Know Occurances :"))
count = 0
for i in tu:
    if(userInput == i):
        count = count + 1
print("The ",userInput," Occurances ", count ," Times ")