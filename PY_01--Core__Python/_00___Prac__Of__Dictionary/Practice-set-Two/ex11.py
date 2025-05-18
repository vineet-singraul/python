# 15. **Check if two keys have the same value.**  
#    **User Input:**  
#    Enter first key: age  
#    Enter second key: years  

#    **Output:**  
#    Both keys have the same value.

data = {"name":"Vineet","Course":"B-Tech","City":"Satna","age":20,"Ending":20}

userKey = input("Enert first key: ")
userkey2 = input("Enter Secand key: ")

userKey = data.get(userKey)
userkey2 = data.get(userkey2)

if userKey == userkey2:
    print("Both Keys have the same value:")