def squares(number):
    return number**2
int_list=[1,2,3,4,5,6,7,8,9,10]

#new_list=[]
# for num in int_list:
#     new_list.append(squares(num))
# print(new_list)

#print([squares(num)for num in int_list])

print(list(map(squares,int_list)))

data1=[100, 200, 300, 400, 500, 600, 700, 800, 900]
data2=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
combination=zip(data1,data2)
for x in combination:
    print(x)
print(list(enumerate(data1,100)))