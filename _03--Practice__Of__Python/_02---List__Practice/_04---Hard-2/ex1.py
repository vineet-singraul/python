# ####1️⃣ **Find the Kth largest element in a list**  
# 👉 **Meaning:** Find the **Kth** (like 1st, 2nd, 3rd, etc.) **largest number** in a list.  
# 🔹 **Example:** `[10, 20, 5, 30]`, `K = 2` → **Output:** `20` (2nd largest number)  


# li = [10, 20, 5, 30]
# count = 1

# def FindList(li):
#     global count 
#     n = li[0]
#     for i in li:
#         if i > n:
#             n = i

#     print(count, "Longest Element in List:", n)
#     li.remove(n)
#     count += 1 

# FindList(li)
# print(li)

# FindList(li)
# print(li)





#  OR   #



li = [10, 20, 5, 30]
li.sort()
n = len(li)
m = li[0]
i = 0
while i < n-1:
   m = li[i]
   i = i + 1
print(m)
