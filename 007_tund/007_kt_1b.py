# Write a program that converts given string to datetime object
import datetime
sample1 = 'Jan 1 2014 2:43PM'
print(f'\nSample1, Input:  ', sample1, '<---',type(sample1))
d=datetime.datetime.strptime(sample1,'%b %d %Y %I:%M%p')
print(f'Output: ',d, '<---',type(d))

sample2 = '14:20 10/12/22'  # YY/MM/DD
print(f'\nSample2, Input:  ', sample2, '<---',type(sample2))
d=datetime.datetime.strptime(sample2,'%H:%M %y/%m/%d')
print(f'Output: ',d, '<---',type(d))

sample3 = 'Tuesday, September 24, 2019'
print(f'\nSample3, Input:  ', sample3, '<---',type(sample3))
d=datetime.datetime.strptime(sample3,'%A, %B %d, %Y')
print(f'Output: ',d, '<---',type(d))

sample4 = '01.01.1970 - 00:00:01'
print(f'\nSample4, Input:  ', sample4, '<---',type(sample4))
d=datetime.datetime.strptime(sample4,'%d.%m.%Y - %H:%M:%S')
print(f'Output: ',d, '<---',type(d))