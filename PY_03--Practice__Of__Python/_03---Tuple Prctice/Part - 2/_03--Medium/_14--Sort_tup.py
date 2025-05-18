# 24. Sort a tuple of numbers `(4, 1, 3, 5, 2)`.

# tu = (4, 1, 3, 5, 2)
  
# Type - 1:
# sor = sorted(tu)
# print(sor)



# Type - 2
tu = (4, 1, 3, 5, 2)
lst = list(tu)
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j] 
tu = tuple(lst)

print("Sorted Tuple:", tu)
