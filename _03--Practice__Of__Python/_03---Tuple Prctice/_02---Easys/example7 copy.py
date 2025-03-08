# 8. **Reverse a tuple without slicing**  
#    **Input:**    
#    Enter a tuple: (1, 2, 3, 4, 5)  

#    **Output:**  
#    (5, 4, 3, 2, 1)  




tu =  (1,2,3,4,5)
li = list(tu)
i = 0 
while i < len(li):
    j = i+1
    while j < len(li):
        li[i],li[j] = li[j],li[i]
        j=j+1
    i=i+1
print(li)