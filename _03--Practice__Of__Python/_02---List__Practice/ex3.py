li = [10, (10, 20, 30), 'Vineet', 50, 70, 90]
times = int(input("Enter Number Time To You Delete :"))
i = 0

while i<times:
    userInput = eval(input("Enter You Want To delete from List : "))
    li.remove(userInput)
    print(li)
print("The Final List " , li)