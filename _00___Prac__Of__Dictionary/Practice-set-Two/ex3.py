# ### 3. **Find all keys that have string values.**  
#    Keys with string values: ['name', 'city']

Diction = {'name': 'vineet', 'age': '20', 'course': 'B-tech', 'Year': '4'}
y = []
keyss = list(Diction.keys())

for x in keyss:
    if Diction.get(x).isdigit():
        continue
    else:
        y.append(x)

print(y)