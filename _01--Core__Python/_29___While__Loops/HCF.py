X = int(input("Enter Num X : "))
Y = int(input("Enter Num Y : "))
Z = int(input("Enter Num Z : "))

q = MinValue = min(X,Y,Z)
i = 1
while i<=MinValue:
    if i%X==0 and i%Y==0 and i%Z==0:
        break

    i = i + 1
    q = q * i
    
print(f'HCF at {X} , {Y} , {Z} is {MinValue}')