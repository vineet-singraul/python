# 13. **Check if Two Strings Are Anagrams**  
#     - Input: `"listen", "silent"`  
#     - Output: `Yes`  


ui1 = input("Enter Fisrt String : ")
ui2 = input("Enter Second String :")

ui1 = sorted(ui1)
ui2= sorted(ui2)

ans = lambda x,y : x == y
if(ans(ui2 , ui1)):
    print("Yas its Anagram : ")
else:
    print("Not A Aanagram : ")