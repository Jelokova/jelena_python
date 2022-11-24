from collections import Counter

sample='aaaaaaaaabbbbbbbcccccccccccdddddddddeeeeeeeeee'
my_counter=Counter(sample)
print(my_counter)
print(my_counter.most_common(2))
#print(list(my_counter.elements()))

from collections import namedtuple
Point=namedtuple('point', 'x,y,z')
pt=Point(2,-1,5)
print(pt)
print(pt.y)