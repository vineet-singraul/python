# 4. **Map & Filter Combined Question:**  
#    Given a list of words `["apple", "banana", "cherry", "date"]`, use `map()` to convert them to uppercase
#    and `filter()` to keep only the words with more than five letters.

li = ["apple", "banana", "cherry", "date"]
ans = map(lambda x: str(x).upper() , li)
print(list(ans))