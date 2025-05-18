# 20. How do you extract even and odd numbers from a list?

li = [1,2,3,4,5,6,7,8,9,10]
ev = [] 
odd = []

for i in li:
    if i%2==0:
        ev.append(i)
    else:
        odd.append(i)

print("Even Number : " ,ev)
print("Odd Number : " ,odd)