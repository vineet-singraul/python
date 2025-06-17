def even(n):
    if n & 1 == 0:
        return True
    else :
        return False
    
n = int(input("Enter A Number :"))
res = even(n)
if res == True:
    print("enen")
else:
    print("odd")