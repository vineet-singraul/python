from math import sqrt,floor

def CalSquarRoot(n):
  return sqrt(n)


n = int(input("Enter A Number :"))
res = CalSquarRoot(n)
print("The Square Root Of Number",n," is : ",floor(res))