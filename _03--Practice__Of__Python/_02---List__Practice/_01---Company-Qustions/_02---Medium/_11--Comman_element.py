# 21. How do you find the intersection of two lists?

li1 = [1,2,3,4]
li2 = [3,4,5,6]

li1 = set(li1)
li2 = set(li2)
print(list(li1.intersection(li2)))