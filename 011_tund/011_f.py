import itertools
letters=['a','b','c','d']
numbers=[1,2,3,4]
names=['Jack','Mary']
numbers2=[4,5,4,3,2,1,0,4]
selectors =[True,False,False,True]
selectors2=[0,1,None,'']

#result=itertools.combinations(letters,3) #порядок не имеет значения
#result=itertools.permutations(letters,2) #порядок имеет значения, символы не повторяются
#result=itertools.product(letters, repeat=4)
# result=itertools.combinations_with_replacement(letters, 4)#порядок не имеет значения,символы повторяются
# for line in result:
#     print(line)

########################
# combined=itertools.chain(letters,numbers,names)
# print(list(combined))
#
# print(letters+numbers+names)
#
# combined=itertools.islice(range(10),1,2)
# print(list(combined))

def more_then_two(x):
    if x>2:
        return True
    return False
# result=filter(more_then_two, numbers2)
# print(list(result))
# result =itertools.compress(letters, selectors)
# print(list(result))
# result2 =itertools.compress(letters, selectors2)
# print(list(result2))
#
# result=itertools.filterfalse(more_then_two,numbers2)
# print(list(result))
#
# result=itertools.dropwhile(more_then_two,numbers2 #обрезать после первого Folse
# print(list(result))
# result=itertools.takewhile(more_then_two,numbers2)#наоборот
# print(list(result))
result=itertools.accumulate(numbers)
print(list(result))
