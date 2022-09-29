numbers=[0,1,2,3,4,5,6,7,8,9]
odds=[]
evens =[]
for num in numbers: #num is any variable ,could be X or Y
    if num % 2==1:
        odds.append(num)
    else:
        evens.append(num)

print(odds)
print(evens)