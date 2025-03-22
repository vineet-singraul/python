# 4. **Reverse a String**  
#    - Input: `"hello"`  
#    - Output: `"olleh"` 

ui = input("Enter A String : ")
ans = lambda x : ui[::-1]
if ans(ui) == ui:
    print("Pailindrom : ")
else:
    print("Not A Pailindrom")