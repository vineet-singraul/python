# Reverse a list
# List: my_list = [1, 2, 3, 4]

# Output:
# [4, 3, 2, 1]  

# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)  
 
             #  OR  #

li = [5,4,3,2,1]
i = 0
l = len(li) - 1

while i < l:
    li[i], li[l] = li[l], li[i] 
    i += 1
    l -= 1

print(li)  
