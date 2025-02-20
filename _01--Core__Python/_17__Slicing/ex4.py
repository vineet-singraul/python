text = input("Enter a word: ")

is_palindrome = text == text[::-1]

if is_palindrome:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
