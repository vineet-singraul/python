# 8. Find the index of `30` in the tuple `(10, 20, 30, 40, 50)`.

tu = (10, 20, 30, 40, 50)

userInput = int(input("Enter A Number To Know Index : "))

for i in tu:
    if(i == userInput):
        print("The Entered Value Is ",userInput," and its index is : ",tu.index(userInput))