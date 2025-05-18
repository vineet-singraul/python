# f = open('f1.py','w')
# f.write("Vineet How Are you Hompe fine :")
# f.close()




# f = open('f1.py','w')
# data = ['hai\n','hello\n','welcome\n']
# f.writelines(data)
# f.write(data) ----> erro dega


# read the data
# f = open('f1.py','r')
# data = f.read(17)
# print(data)


# data = f.read()
# print(data)
# data = f.read()
# print(data)



# data = f.readline()
# print(data)

# data = f.readlines()
# print(data)









# curser movment 
# f = open('f2.txt','a')
# # tell() ----> curser current location 
# # seek() ----> movement of curser
# print(f.tell())
# f.write("hi")
# print(f.tell())
# f.close()





f = open('f3.txt','a+')
print(f.tell())
# f.write("hhhhhhh")
print(f.tell())
f.write("welcome")
print(f.tell())
f.seek(0)
print(f.tell())
data = f.read(10)
print(data)