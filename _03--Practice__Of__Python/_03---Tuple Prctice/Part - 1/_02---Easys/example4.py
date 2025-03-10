







# 5. **Check if all elements are positive**  
#    **Input:**  
#    Enter a tuple: (1, 2, 3, -4, 5)  

#    **Output:**  
#    False  


tu = input("Enter A Tuple Elements : ").split()
tu = list(tu)

li = []  
pos = []  

for i in tu:
    if int(i) < 0:
        li.append(i) 
    else:
        pos.append(i) 

print("All Positive Number :", tuple(pos))
print("All Negative Number :", li)
