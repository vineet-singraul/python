# 11. How do you sort a list in ascending and descending order?

li = [-5,4,30,28678678,1]

i=0
while i<len(li)-1:
    j=i+1
    while j<len(li):
        if(li[i]>li[j]):
            li[i] , li[j] = li[j] , li[i]
        j+=1
    i+=1
print(li)



# -----------------------------------

li.sort()
print(li)