







# output element is always equal to one element
# output me only single element return aayega


str = "Vineet"
m = len(str)
i = 0
li = []
while i < m:
     r = str.index(i)
     print(i)
     li.append(r)
     i = i + 1
print(li)