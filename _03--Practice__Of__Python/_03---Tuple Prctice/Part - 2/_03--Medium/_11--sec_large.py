# 21. Write a function that returns the second-largest element from a tuple `(10, 20, 5, 40, 30)`.

# tu = (10, 20, 5, 40, 30)
# n = tu[0]
# for i in tu:
#     if i>n:
#         n = i
# for j in tu:
#     m = tu[0]
#     if j > m and m<n :
#         m = j
# print("Second Largest  : ",m)















#   Using function

tu = (10, 20, 5, 40, 30)
srt = sorted(tu)
print("Second Largest : ",srt[len(srt)-2])
