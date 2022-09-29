# Write a program to print yesterdays, today and tomorrow dates
import datetime
today=datetime.date.today()
tdelta= datetime.timedelta(hours=24)

print(f'Yesterday: ', today-tdelta)
print(f'Today: ',today)
print(f'Tomorrow: ', today+tdelta)
