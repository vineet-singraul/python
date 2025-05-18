# 12. Find the sum of all elements in the tuple `(10, 20, 30, 40, 50)`.

# tu = (5,4,1,2,3)
# tu1 = tuple(sorted(tu))

# print(tu1[0])
# print(tu1[len(tu1)-1])




#    or 

tu = [5,4,3,-1,0]
i = 0
while i<len(tu)-1:
    j=i+1
    while j<len(tu):
        if(tu[i] > tu[j]):
            tu[i], tu[j] = tu[j] , tu[i]
        j+=1
    i+=1
print(tu)
print("Min Value In Tuple  : ",tu[0])
print("Max Value In Tuple  : ",tu[len(tu)-1])