# 29. Write a function that checks if all elements in a tuple are integers.

tu = (1, 2, 3, 4, 6)
l = len(tu)
count = 0
for i in tu:
    if type(i) == int:
        count = count + 1

if(count == l):
   print("Tuple Present Element In Number :")
else:
   print("Something Present in String in tuplle")