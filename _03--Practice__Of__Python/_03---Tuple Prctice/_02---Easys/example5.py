# 6. **Find the length of the longest word in a tuple**  
#    **Input:**   
#    Enter a tuple: ("apple", "banana", "cherry", "strawberry")  
 
#    **Output:**  
#    10  

 
tup = input("Enter a tuple : ").split()
print("Your Entered Tuple : ",tuple(tup))
n = len(tup[0])
li = []
for i in tup:
    if n < len(i):
        li.append(i)
        le = len(i)
print("The Max Len String Is In Tuple : ",li," : ",le)
