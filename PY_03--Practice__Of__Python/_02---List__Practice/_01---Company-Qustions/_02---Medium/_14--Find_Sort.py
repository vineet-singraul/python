# 24. How do you check if a list is sorted/?

li = [1,12,3,4,5,6,7]
n = li[0]
for i in li:
    if i>= n:
        n=i
        f = True
    else:
        f = False

if f:
    print("All List value in assending order :")
else:
    print("Not a assending order")