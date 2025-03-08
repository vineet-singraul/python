# 18. How do you merge two lists alternatively?  
#    *(Example: `[1,2,3]` and `[a,b,c]` → `[1,a,2,b,3,c]`)*

li1 = [1,2,3]
li2 = ['a','b','c']
li3 = []
for i in li1:
    li3.append(i)
    for j in li2:
        li3.append(j)
print(li3)