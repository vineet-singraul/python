# n = 1
# i = 5
# while i >= 0:
#     print(' '*(n-1) + '*'*i)
#     i = i - 1
#     n = n + 1


#  * * * * *
#    * * * *
#      * * *
#        * *
#          *


#      OR

n = 5
i = 0
while i<=n:
    print(' '*i + '*'*(n-i))
    i = i + 1