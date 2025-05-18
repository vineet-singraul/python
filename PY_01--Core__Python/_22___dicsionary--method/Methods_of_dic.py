d1 = {1:"Vineet" , 2:"Mohni", 3 : "Anmol"}


print(id(d1))
print("The Copy Of Dictionary : ", id(d1.copy())) 
print("The Copy Of Dictionary : ", d1.copy()) 


print("Clear All the Data Of Dictionary : ",d1.clear())
print(d1)


d2 = {1: "Vineet", 2: "Mohni", 3: "Anmol"}
userInput = int(input("Enter The Key: "))  
out = d2.get(userInput, "Key Not Found")  
print(out)

y = d2[4] = "Mahek"
print(y)
print(d2)

d2 = {1: "Vineet", 2: "Mohni", 3: "Anmol"}
userInput1 =input("Enter The Key: ")
out = d2.keys(userInput1) 
print(out)


d2 = {1: "Vineet", 2: "Mohni", 3: "Anmol"}
print(d2.pop(1))
print(d2)



d = {1: "Vineet", 2: "Mohni", 3: "Anmol"}
print("Before popitem:", d)


removed_item = d.popitem()

print("Removed Item:", removed_item)
print("After popitem:", d)


d = {1: "Vineet", 2: "Mohni", 3: "Anmol"}
d.update({4: "Mahek", 5: "Jiya"})  
print(d)
