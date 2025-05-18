i = 1
n = 10
sum = 0
while i<=10:
    sum = sum + i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
    i = i + 1
print(sum)