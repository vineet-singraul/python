# Calculate the factorial of a number using math.factorial().
from math import factorial
def myfactorial(n):
    return factorial(n)

n = int(input("Enter Number :"))
res = myfactorial(n)
print("The Fectorial Number Is : ",res)