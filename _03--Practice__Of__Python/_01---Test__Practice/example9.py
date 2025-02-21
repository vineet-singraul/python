# Example 1: Write a program to display n natural numbers. (In Horizontal-1,2,3,4,5……. )


input1 = -1
i = 2
print(input1 , end=" ")
while input1 < i:
    print(i,end=",")
    i=i+1
    if(i == 6):
      break