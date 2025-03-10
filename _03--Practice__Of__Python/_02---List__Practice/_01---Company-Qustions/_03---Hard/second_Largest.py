# 31. How do you find the second largest and second smallest element in a list?


# li = [-1,20,5,13,4]
# m = li[0]
# n = li[0]
# for i in li:
#     if i>n:
#         n=i
# for j in li:
#     if j>m and j<n:
#         m = j
# print(m)


# li = [1,2,5,4,3]
# n = len(li)-1
# li1 = sorted(li)
# print(li[n-1])


li = [1,2,5,3,4]
n = li[0]
m = max(li)

for i in li :
    if i>n and i<m:
        n = i
print(n)