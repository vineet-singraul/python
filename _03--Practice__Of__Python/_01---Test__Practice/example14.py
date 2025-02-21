# Example 7: Write a program to find how many vowels and consonants are present in strings.

def findVovelConsnt(userInput,lenOfString):
    vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
    i = 0
    VovCount = 0 
    ConsoCount = 0
    while i < lenOfString:
        if userInput[i] in vowels:
            VovCount += 1
        else:
            ConsoCount += 1
        i += 1
    print("The Total Vovels In String : ",VovCount)
    print("The Total Consonent In String : ",ConsoCount)
userInput = input("Enter A String : ")
lenOfString = len(userInput)
findVovelConsnt(userInput,lenOfString)

