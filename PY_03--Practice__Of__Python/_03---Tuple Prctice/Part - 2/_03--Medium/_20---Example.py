# 31. Convert a tuple of numbers into a tuple of their squares.
userInput = tuple(map(int, input("Enter A Tuple: ").split()))  
li = []
for i in userInput:
    i = int(i) ** 2  
    li.append(i)
li = tuple(li) 
print("The Square Is:", li)
