isikukood='47506220254'
#print(type(isikukood))
isikukood=list(map(int,isikukood))
#print(type(isikukood))
#isikukood=[isikukood]
# print(type(isikukood))
print(isikukood)
check1=[1,2,3,4,5,6,7,8,9,1,0]
check2=[3,4,5,6,7,8,9,1,2,3,0]
#print(type(check1))
check_list1 = [x*y for (x, y) in zip(isikukood,check1)]
print(check_list1)
check1_sum=sum(check_list1)
print(check1_sum)
#print(check1_sum//11)
control_num=(check1_sum-((check1_sum//11)*11))
print(control_num)
if control_num==isikukood[10]:
    print('ok')
else:
    print('contin')
