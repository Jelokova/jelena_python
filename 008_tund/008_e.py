# write method
#with open("testtext.txt",'w',encoding="utf-8") as file:
    # file.write("Hello world\n")
    # file.write("Hello planet")
    # file.seek(4)
    # file.write('*****')
#NB!Method write date from file

# append method (dded all date to the end)
# with open("testtext2.txt", 'a', encoding="utf-8") as file:
#     file.write("Hello world\n")
#     file.write("Hello planet")
#     file.write('*****')

#method create
import datetime
try:
    with open(f"test{datetime.date.today()}.txt", 'x', encoding="utf-8") as file:
        file.write('Hello world!')
        file.seek(0)
        file.write('******')
except:
    with open(f"test{datetime.date.today()}.txt", 'a', encoding="utf-8") as file:
        file.write(str(datetime.datetime.now())+'\n')
