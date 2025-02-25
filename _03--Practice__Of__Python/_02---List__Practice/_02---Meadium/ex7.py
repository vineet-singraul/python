# 19. **Convert a list to a string**  
#     **List:** `my_list = ["hello", "world"]`  

#     **Output:**  
#     hello world  


li = ["hello", "world"]
print("Befor Performe Type Conversion : ",type(li))
print(li)
print("--------------------------------------")
st = " ".join(li) 
print("After Performing Type Conversion:", type(st))
print(st)