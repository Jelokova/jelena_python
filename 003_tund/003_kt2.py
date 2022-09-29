x = range(101)
fizz=[]
buzz =[]
fizz_buzz=[]
for n in x[1:]:
    if ((n/3) - (n//3))==0 and ((n/5) - (n//5))==0:
        fizz_buzz.append(n)
    elif ((n / 3) - (n // 3)) == 0:
                fizz.append(n)
    elif ((n / 5) - (n //5)) == 0:
                buzz.append(n)

for z in fizz_buzz:
    z = str(z)
    print(z + ' FizzBuzz')

for x in fizz:
    x=str(x)
    print(x+' Fizz')

for y in buzz:
    y = str(y)
    print(y + ' Buzz')
