# 9. **Find the smallest element in a tuple**  
#    **Input:**   
#    Enter a tuple: (10, 5, 20, 1, 30)   
#  
#    **Output:**  
#    1  

tu = (10, 5, 20, 1, 30)
li = list(tu)

li.sort()
print(li)

print("Smollest Value In Tuple : " ,li[0])