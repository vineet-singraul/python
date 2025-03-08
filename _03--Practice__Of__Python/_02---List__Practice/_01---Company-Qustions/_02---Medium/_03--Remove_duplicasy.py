# 13. How do you remove duplicates from a list?

li = [1,2,3,3,2,1,5]
li.sort()
i = 0 
while(i<len(li)-1):
    j = i +1
    while(j<len(li)):
        if(li[i] == li[j]):
            li.remove(li[j])
        j+=1
    i+=1
print(li)