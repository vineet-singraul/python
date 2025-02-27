# l1 = [1,2,3,4]
# x = list(map ( lambda x : "Even" if x%2==0 else "Odd",l1))
# print(x)



l1 = [1,2,3,4]
x = list(filter ( lambda x : x if x%2==0 else None , l1))
print(x)


l1 = [1,2,3,4]
x = list(filter ( lambda x : x if x%2==1 else None , l1))
print(x)




from functools import reduce
l1 = [1,2,3,4]
x = reduce(lambda x,y : x if x>y else y ,l1)
print(x)


l1 = [1,2,3,4]
x = reduce(lambda x,y : x if x>y else y ,l1)
print(x)





x = lambda p : [i for i in range(2,p+1,2)]
print(x(10))