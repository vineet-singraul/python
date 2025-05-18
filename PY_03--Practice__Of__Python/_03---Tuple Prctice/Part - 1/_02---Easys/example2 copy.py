



# 2. **Get the first and last elements of a tuple**  



tu = (1, 5, 2, 3, 6, 8, 23)

n = tu[0]  
m = tu[0] 

for i in tu:
    if i > n:
        n = i
    if i < m: 
        m = i

print("Largest Number:", n)
print("Smallest Number:", m)


