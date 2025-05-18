# 18. Find the index of the first occurrence of `5` in `(1, 2, 5, 3, 5, 4, 5)`.

tu = (1, 2, 5, 3, 5, 4, 5)

userInput = (int(input("Enter value to find occurance : ")))

if userInput in tu:
    print("Entered number is ",userInput," and its index is : ",tu.index(userInput))