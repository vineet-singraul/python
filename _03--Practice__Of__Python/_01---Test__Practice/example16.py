userInput = eval(input("Enter The List :"))

for i in userInput:
    if str(i).isdigit():
        print(i)