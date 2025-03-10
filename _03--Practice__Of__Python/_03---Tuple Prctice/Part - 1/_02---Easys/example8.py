tu =  (5,4,3,2,1)
li = list(tu)
i = 0 
while i < len(li):
    j = i+1
    while j < len(li):
        if(li[i] > li[j]):
            li[i],li[j] = li[j],li[i]
        j=j+1
    i=i+1
print(li)