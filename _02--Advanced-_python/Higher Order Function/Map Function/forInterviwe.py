li1 = [1,2,3,4,5]
li2 = [2,3,4,5]
li3 = [1,2]

def Add(x,y,z):
    return x+y+z

p = tuple(map(Add, li1,li2,li3))

print(p)



# first loop me 1,2,1 add ker diya and second iteration me 2,3,2 ko plus kiya

# map bus ek ek object genrate karata hai uske under  value store karta hai 