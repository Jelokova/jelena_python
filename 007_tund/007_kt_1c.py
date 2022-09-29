import datetime
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'
input=[sample1,sample2,sample3,sample4]
print(input)
for x in input:
    print(f'\nInput:',x,type(x))
    if x ==sample1:
        d=datetime.datetime.strptime(sample1,'%b %d %Y %I:%M%p')
        print(f'Output: ', d, '<---', type(d))
    elif x ==sample2:
        d = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
        print(f'Output: ', d, '<---', type(d))
    elif x ==sample3:
        d = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
        print(f'Output: ', d, '<---', type(d))
    elif x == sample4:
        d = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
        print(f'Output: ',d, '<---',type(d))


