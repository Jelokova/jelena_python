x=100
if x==5:
    print('X is five')
elif x!=100:
    print('X is not 100')
else:
    print('All conditions are False!')

x = '23876543987'
if len(x) == 11:
    print(x)
elif len(x) != 11:
    if len(x)>11:
        print(x, 'is too long')
    else:
        print(x,'is too short')
    print('try again!')

###########

x=5
if 10 > x > 2:
    print('Yes')

x=11
if  not x<10:
    print("Y")
