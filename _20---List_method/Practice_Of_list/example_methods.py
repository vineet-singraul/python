li = [10,20,30,40,50]

# Append methos used
li.append(100)
print(li)

# Expend method used
li.extend([100,200])
li.extend(("Vineet","Riya"))
print(li)


# insert method used
li.insert(2,1000)
print(li)



# copy method used
li2 = li.copy()
print(id(li))
print(id(li2))


# remove method used
counts = li.count(100)
print("Count is : ",counts)


# sort method used
sortforli = [100,20,30,40,50]
sortforli.sort()
print("Sotrted List is : ",sortforli)


