# 5. **Write a Python program that adds corresponding elements of two lists using `map()`.**  
#    - **Input:** `[1, 2, 3]` and `[4, 5, 6]`  
#    - **Output:** `[5, 7, 9]`  



def AddList(li1,li2):
    return li1 + li2
     

li1 = [1,2,3]
li2 = [4,5,6]
ans = map(AddList , li1, li2)
print(list(ans))