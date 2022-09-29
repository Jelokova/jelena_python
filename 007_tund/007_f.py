import datetime
# today= datetime.datetime.today()
# print(today.strftime('%A %d,%B %Y'))

dstr ='November 30, 2022 17:15'
print(dstr)
print(datetime.datetime.strptime(dstr,'%B %d, %Y %H:%M'))

# print(datetime.datetime.fromtimestamp(123456))
# print(today.timestamp())