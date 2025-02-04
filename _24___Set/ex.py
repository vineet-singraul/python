# s = {10,20,30,"Vineet","riya",10,20}
# print(s)
# print(type(s))


s1 ={10,20,30,40,50,60}


# Python  element
# print("Max Value In Set : ",max(s1))  # 60
# print("Min Value In Set : ",min(s1))  # 01
# print(" Sum Value In Set : ",sum(s1))  # 01
# print(" type Value In Set : ",type(s1))  # 01



# set Method
# copt = s1.copy()
# print("Copy In Set",copt)
# Copy In Set {50, 20, 40, 10, 60, 30}

# print(s1.clear())
# print(s1)
# set()


s2 ={10,60}
s2.update("Vineet")
# {40, 10, 't', 50, 'V', 20, 'e', 'i', 60, 'n', 30}
s2.update([10,20,30,40,50,"vineet"])
# {40, 10, 'vineet', 'V', 60, 't', 50, 20, 'e', 30, 'i', 'n'}
print(s2)



s2.remove(10)
print(s2)
# {'i', 40, 't', 'V', 'e', 'n', 50, 20, 'vineet', 60, 30}



s2.discard("vineet")
print(s2)
{'i', 40, 't', 'V', 'e', 'n', 50, 20, 60, 30}



s2.pop()
print(s2)
# {'i', 40, 't', 'V', 'e', 'n', 50, 20, 60, 30}

