#  find squre root of given no

def chackSquarRoot(userInput):
    if userInput > 0 :
       userInput = userInput**0.5
       print(f'The Squar Root Is : {int(userInput)}')


userInput = int(input("Enter The Number :"))
chackSquarRoot(userInput)


