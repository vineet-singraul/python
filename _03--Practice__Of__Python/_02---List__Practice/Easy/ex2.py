time = int(input("How Number You Want To Add On List :"))
li = []

i = 0 
while i<=time:
    userInput  = eval(input("Enter Something To add On the List : "))
    li.append(userInput)
    i = i + 1

print("Total Items In List", li)


# How Number You Want To Add On List :5

# Enter Something To add On the List : 10
# Enter Something To add On the List : (10,20,30)
# Enter Something To add On the List : "Vineet"
# Enter Something To add On the List : 50
# Enter Something To add On the List : 70
# Enter Something To add On the List : 90

# Total Items In List [10, (10, 20, 30), 'Vineet', 50, 70, 90]