# 5. Check if the number `5` exists in the tuple `(1, 2, 3, 4, 5)`.

tu = (1,2,3,1,4,5,6,7,8,9)
userInput = int(input("Enter Num for check "))

if(userInput in tu):
    print("Yas")
else:
    print("No")