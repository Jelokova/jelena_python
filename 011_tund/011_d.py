import itertools
counter=itertools.count(start=0.5,step=0.5)
print(next(counter)) #Генератор счётчика
print(next(counter))
print(next(counter))
print(next(counter))
data=[100,200,300,400,500]
data2=zip(itertools.count(100,-10), data)
print(list(data2))
data3=list(itertools.zip_longest(data,range(10)))
print(data3)