import itertools

#counter=itertools.cycle(['on','off'])
counter = itertools.repeat('Hello' ,times=5)
print(next(counter))
print(next(counter))
print(next(counter))

counter2=itertools.cycle(['on','off'])
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(list(zip([1,2,3,4,5,6], counter2)))

def squares(num1,num2):
    return num1**num2

x=[(0,2),(7,3),(5,9),(1,1)]
print(list(itertools.starmap(squares, x)))
print(list(map(squares,range(10),itertools.repeat(3))))
print(list(map(squares,range(10),itertools.cycle([3,2]))))

for x in itertools.repeat(3,times=10): # выдаст 10 троек
    print(x)
