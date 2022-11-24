# from collections import defaultdict
# default=defaultdict(int)
# default['a']=1
# default['b']=2
# print(default['c'])
# dict_def={'name':'Jack'}
# print(dict_def)

from collections import deque
d=deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
x=d.popleft()

print(x)
print(d)

d.extendleft([4,5,6,7])
print(d)
d.rotate(1) #сдвиг на 1
print(d)