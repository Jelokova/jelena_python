def say_hello(name,surname):
    print(f'Hello {name} {surname}!!!')
say_hello ('Roman', 'Kuts')

def fizz_buzz(start, stop):
    for x in range (start, stop + 1):
        if x % 15==0:
            print(x,'FizzBuzz')
        elif x % 3==0:
            print(x,'Fizz')
        elif x % 5==0:
            print(x, 'Buzz')

fizz_buzz(10,100)
