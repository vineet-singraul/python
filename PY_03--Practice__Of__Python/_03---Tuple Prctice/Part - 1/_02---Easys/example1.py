# 1. **Check if a tuple is empty**  
#    **Input:**  
#    Enter a tuple: ()  

#    **Output:**  
#    True  


tu = ("Vineet", "Mohni")  # Tuple of names
inp = input("Enter the Name to Check: ")  # Taking input as a string

if inp in tu:  # Checking if input is present in the tuple
    print("Yes, it's present in the tuple.")
else:
    print("No, it's not present in the tuple.")
