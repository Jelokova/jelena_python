# 1 Task
# name=input('Enter your name: ')
# surname=input('Enter your surname: ')
# age=input('Enter your age: ')
# print (f'Hello, {surname} {name}. Your age is: {age}')

# 2 Task
# a=int(input('Enter side a: '))
# b=int(input('Enter side b: '))
# c = 0.5*(a**2 + b**2)
# print(c)

# 3 Task
# a=float(input('Enter side a: '))
# b=float(input('Enter side b: '))
# c=float(input('Enter side c: '))
# if c**2 == (a**2 + b**2):
#     print('Right triangle')
# else:
#     print('NOT Right triangle')

# 4 Task ?????
# sample_list=[]
# sample_list=(input('Enter list values using spase as separator: '))
# print(sample_list)
# for x in (sample_list[::-1]):
#     print(x)

# # Task 5
# tuple1=(1,2,3,4,5,6)
# tuple2=(10,20,30)
# new_tuple = tuple1[0:2] + tuple2 + tuple1[3:]
# print(new_tuple)

# # Task 6
# a=[1,2,2,3,3,4,4]
# max_count=0
# for num in a:
#     if a.count(num)>max_count:
#         max_count=a.count(num)
# res=[]
# for num in a:
#     if a.count(num)==max_count and num not in res:
#         res. append(num)
# print(res)

#Task 7
sec = 1234565
days = sec // (24*3600)
sec %= (24*3600)
print(sec)
hours = sec // 3600
sec %=3600
print(sec)
min =sec/60
sec %=60
print(sec)
print(f'{days}:{hours}:{sec}')