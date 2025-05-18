# li = {'name':"vineet", 'age':34 , 'quali':'M-Tech'}


# # fir gatting value
# getName = li.get('name')
# print(getName)



# # # for updating the value
# # li.['name'] = 'Puneet'
# # print(li)


# # like we want to number of keys know
# print("Number Of Keys", li.keys())



# # keval hame value cahiye to
# print("Total Keys in Dictionary : " , li.values())



# # total items janana hai to 
# print("Total items janana hai : " , li.items())



# # pop(argument pass hare) -->  
# print(li.pop('name'))
# print()



# # popitems() -->  last ky value remove ker dega
# # print(li.popitem())



print("===========================================================")
di = {'name':'vineet' , 'age':34 , 'quali':'M-Tech'}

print()
# fromkeys() --->  
di.setdefault('name','vin')
print(di)
# {'name': 'vineet', 'age': 34, 'quali': 'M-Tech'}  ----> koi update nhi hoga


# update()
di.update({'name':'Rahul'})
# {'name': 'Rahul', 'age': 34, 'quali': 'M-Tech'}  --->  update ho raha hai  
di.update({'name':'Rahul','age':'45'})
# {'name': 'Rahul', 'age': '45', 'quali': 'M-Tech'}  naya paire genrate ker sakte hai 
print(di)




# fromkeys() --->  unic ele colooection hai 
s = 'vineet'
x = dict.fromkeys(s)
print(x)
# {'v': None, 'i': None, 'n': None, 'e': None, 't': None}  --- > ek naya array deta hai
x = dict.fromkeys(s,50)
print(x)
# {'v': 50, 'i': 50, 'n': 50, 'e': 50, 't': 50}


