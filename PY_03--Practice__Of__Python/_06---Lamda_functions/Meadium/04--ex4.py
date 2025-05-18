# 14. **Find the Fibonacci Number at Nth Position**  
#     - Input: `6`  
#     - Output: `8`  


from functools import lru_cache

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)

ui = int(input("Enter a number to check Fibonacci: "))
print(fib(ui))
