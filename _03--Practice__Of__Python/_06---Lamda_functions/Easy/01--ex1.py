# 1. **Sum of Two Numbers**  
#    - Input: `5 3`  
#    - Output: `8`  


sum_of_two = lambda x, y: x + y
a, b = map(int, input("Enter two numbers: ").split())
print("Sum:", sum_of_two(a, b))