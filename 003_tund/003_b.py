courses =['History','Match', '222', '4512', 'Litherature', 'Physics', 'Programmimg','Litherature']
nums=[1,5,6,8,3,4,2]

# courses.reverse() #changed value
# print(courses[::-1]) # only on screen
# print(courses)
# courses.sort() #accesing
# print(courses)
# courses.sort(reverse=True)#deccesing
# print(courses)
# print(sorted(courses))#not change original sourse
# print(courses)

print(min(courses))
print(max(courses))
print(sum(nums))

print(courses.index('Litherature',7,9))
print('222'in courses)# return true or false if value exist in list, 100% match
print('_'.join(courses))
print('\n'.join(courses))
lst_str = ', '.join(courses)
print(lst_str)
print(lst_str.split(', '))
print(courses[0:3]+ courses[-3:])

courses2 = courses.copy() # create copy on list
courses2[0]='Art'
courses[1]='Art2'
print(courses2)