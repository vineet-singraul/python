# 11. **Remove duplicates from a list**  
#     **List:** `li = [1, 2, 2, 3, 4, 4, 5]`  

#     **Output:**  
#     [1, 2, 3, 4, 5]  



# li =eval(input("Enter A List Where You want To Remove Duplicasy :"))
li =[10,20,10,20,30,40,30,40,50]
i = 0 
while i < len(li):
    j = i+1
    while j < len(li):
        if li[i] == li[j]:
            li.remove(li[i])
        else:
            j+=1
    i+=1
print(li)




