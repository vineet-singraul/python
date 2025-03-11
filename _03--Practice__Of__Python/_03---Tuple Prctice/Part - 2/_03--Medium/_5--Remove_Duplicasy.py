# 15. Remove duplicates from the tuple `(1, 2, 3, 2, 4, 1, 5, 3)`.



# def lens(tu):
#     count = 0
#     for i in tu:
#        count += 1
#     return count
    

# tu = (1, 2, 3, 2, 4, 1, 5, 3,-1,-1)
# tu = list(tu)
# i = 0
# while(i < lens(tu)-1):
#     j=i+1
#     while(j<lens(tu)):
#         if(tu[i] == tu[j]):
#             tu.pop(j)
#         j+=1
#     i+=1
# print(tuple(tu))












tu = (1, 2, 3, 2, 4, 1, 5, 3, -1, -1) 

li1 = []  

for i in tu:
    if i not in li1: 
        li1.append(i)

tu = tuple(li1)  
print(tu)
