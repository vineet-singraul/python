# 7. **Check if a tuple contains only unique elements**  
#    **Input:**  
#    Enter a tuple: (10, 20, 30, 40, 50, 10)  
 
#    **Output:**  
#    False  

tu = input("Enter The Tuple : ").split()
i = 0
while i < len(tu):
    j = i + 1
    while j < len(tu):
        if tu[i] == tu[j] :
            print("False")
        j+=1
    i+=1