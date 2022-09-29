# empty_list =[3]
# empty_list2 = list()
# print(bool(empty_list)) # list is boolean

# world='world'
# filled_list=[1, 0.2,'hello',[1,2,[2,3,4],3,4,5],world, True, None,True]
# print(len(filled_list))
# print(filled_list[3])
# print(filled_list[3][2][0])

############################################
courses =['History','Match', 'Litherature', 'Physics', 'Programmimg']
nums=[1,5,6,8,3,4,2]
# test_lst = [1,2,3]
# print(test_lst[1])
# test_lst[1]= 777
# print(test_lst)
print(courses)
courses.append('Art') #add to the end of list
print(courses)
#courses.append(['Art','Biology']) #insert new list
#print(courses)
courses.insert(1,'Biology') #add to exact please, but changed other indexes
courses.extend(['BBio', 'BBB']) #add more than one value, to the end of list only
courses.extend('everyletter separatly')
print(courses)

courses.remove('Biology') #remove first NB! not possible to repair
print(courses)
##(#)#courses.remove(courses[0:-13]) #remove with index
print(courses)
popped_item = courses.pop(0)
print(popped_item)
print(courses)
