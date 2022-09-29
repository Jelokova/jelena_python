import datetime
d=datetime.date(2022,9,20)
print(d)
today=datetime.date.today()
print(today)
print(today.month)
print(today.day)

print(today.weekday()) #Дни недели с 0-6
print(today.isoweekday()) #Дни недели с 1-7
print(today-d)

tdelta = datetime.timedelta(days=7,hours=12)
print(today+tdelta)

bday= datetime.date(2023,3,16)
till_bbday = bday - today
print(till_bbday)
print(till_bbday.days)
print(till_bbday.total_seconds())
