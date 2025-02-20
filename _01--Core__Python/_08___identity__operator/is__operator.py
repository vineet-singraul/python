#  is operator memory address compare karta hai 
x = 10
y = 10
print(id(x))   #140703410436824
print(id(y))   #140703410436824
print(x is y)  #True




a = [10]
b = [10]
print(id(a))    #1221705587008
print(id(b))    #1221705585024
print(a is b)   #False