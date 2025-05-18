number = int(input("Enter one Subject Marks : "))

if number>100 or number<0:
    print("Enter Valid Number : ")
else:
    if number>=60 and number<=100:
      print(f'{number} First Division Pass :')
    elif number>=45 and number<=60:
      print(f'{number} Second Division Pass :')
    elif number>=35 and number<=45:
      print(f'{number} Thired Division Pass :')
    elif number>=0 and number<=35:
       print(f'{number} Your Failed : ')    