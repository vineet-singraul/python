# 26. Write a function that removes a specific element from a tuple.


tu = (1, 2, 3, 4, 5)
li = list(tu)
ui = int(input("Enter a number to delete: "))
if ui in li:
    li.remove(ui)
tu = tuple(li)
print("Updated Tuple Is:", tu)








