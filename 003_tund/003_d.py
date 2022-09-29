courses ={'History','Math', 'Litherature', 'Physics', 'Programmimg','Litherature'}
nums={1,5,6,8,3,4,2}
#####SET####

empty_set = {1}
print(type(empty_set))
print(courses)
print(nums)

a=courses.pop()
print(a)

#courses.clear()
#print(courses)

set1 = {'History','Math', 'Litherature', 'Physics'}
set2 = {'Programming','Math', 'Litherature', 'Bilogy'}

print(set2.intersection(set1))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.union(set2)) #create list frpm two sets, removed dublicate
set1.update(('Hello','NNN'))
print(set1)

a=[1,3,3,5,6,8,4,5,6,7,7,]
print(list(set(a))) #remoe dublicate from the list