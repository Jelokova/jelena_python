import time
input='20221003202125'

#print(type(input))
dt =time.strptime(input, '%Y%m%d%H%M%S')
#print(dt)
#print(type(dt))
print(f'Input string is:', input,' or ',time.strftime('%Y-%m-%d %H:%M:%S', dt))
# #sample1 = 'Jan 1 2014 2:43PM'
d=time.strftime('%b %d %Y %I:%M%p',dt)
print("Sample1:", d)

# #sample2 = '14:20 10/12/22'  # YY/MM/DD
d=time.strftime('%I:%M %Y/%m/%d',dt)
print("Sample2:", d)
#
# #sample3 = 'Tuesday, September 24, 2019'
d=time.strftime('%A, %B %d, %Y',dt)
print("Sample3:", d)
#
# #Sample4 = '01.01.1970 - 00:00:01'
d=time.strftime('%d.%m.%Y - %I:%M:%S',dt)
print("Sample4:", d)
#
#
