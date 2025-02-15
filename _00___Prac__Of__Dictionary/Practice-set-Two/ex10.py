# 14. **Convert a dictionary to a list of tuples.**  

#    Dictionary as tuples: [('name', 'Alice'), ('age', '25')]

data = {"name":"Vineet","Course":"B-Tech","City":"Satna","age":20,"Ending":2025}

datas = data.items()
li = list(datas)
print(tuple(li))