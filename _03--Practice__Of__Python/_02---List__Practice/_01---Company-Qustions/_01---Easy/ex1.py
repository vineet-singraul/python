# How do you remove duplicates from a list while maintaining order?

li = [1,2,3,4,6,1,3,4,2]
li.sort()
print(li)
i = 0 
while i<len(li):
    j=i+1
    while j<len(li):
        if(li[i]==li[j]):
            li.remove(li[j])
        j=j+1
    i=i+1
print(li)