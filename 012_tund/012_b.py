import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='python10'
)
my_cursor = mydb.cursor()
my_cursor.exicute('SELECT * FROM student')
for x in my_cursor:
    print(x)

result = my_cursor.fetchall()
print(result)

result1=my_cursor.fetchone()
print(result1)
result2=my_cursor.fetchone()
print(result2)
result3=my_cursor.fetchone()
print(result3)
result4=my_cursor.fetchone()
print(result4)

while result:
    print (result)
    result= my_cursor.fetchone

result=my_cursor.fetchmany(5) #first 5 rows
print(result)