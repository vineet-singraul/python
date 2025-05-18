# # 8. Write a program to check if the given strings are anagram or not. 

name1 = input("Enter A String 1 : ").lower()
name2 = input("Enter A String 2 :").lower()


if(sorted(name1) == sorted(name2)):
    print("Enter String Is anagram")
else:
    print("Enter String Is Not anagram")
