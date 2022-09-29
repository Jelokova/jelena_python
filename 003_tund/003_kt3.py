x = range(101)
for n in x[1:]:
    if ((n/3) - (n//3))==0 and ((n/5) - (n//5))==0:
        print(n, 'FizzBuzz')
    elif ((n / 3) - (n // 3)) == 0:
        print(n,'Fizz')
    elif ((n / 5) - (n //5)) == 0:
        print(n, 'Buzz')

