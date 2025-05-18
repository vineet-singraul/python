# 7. How do you check if an element exists in a list
# userInput = int(input("Enter Number:"))
# li = [1,2,3,4,5,6,7]
# for i in li:
#     if(i == userInput):
#       print("YAS")







userInput = int(input("Enter Number:")) 
li = [1, 2, 3, 4, 5]
[print("YAS") for i in li if i == userInput]