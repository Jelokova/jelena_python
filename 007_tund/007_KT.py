"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import datetime

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'



# Write a program to print yesterdays, today and tomorrow dates


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
print(datetime.datetime.fromtimestamp(some_day),strftime(%d.%m.%y))


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
def minus_two_weeks(st):
    date=datetime.datetime.fromtimestamp(ts)
    date-=datetime.timedelta(weeks=2)
    return datetime.datetime.timestamp(date)
print(minus_two_weeks(1014163200))