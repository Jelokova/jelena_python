import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678'
    database='python10'
)
print(mydb)
my_cursor = mydb.cursor()
my_cursor.exicute('create database python10')
my_cursor.exicute('SHOW DATABASES')
for db in my_cursor:
print (db)
my_cursor.exicute('CREATE TABLE student(name VARCHAR(255), age INTEGER(10))')
my_cursor.exicute('INSERT INTO student(name,age)VALUES("Roman",34)')
mydb.commit() #only here added all value above this record
#or
mydb.autocommit = True
student1=('Mary',20)
my_cursor.exicute('INSERT INTO student(name,age)VALUES(%s,%s)'student1)
student_lst = [(Sarah),18],('Jerry',23), ('Bob',30)]
my_cursor.exicutemany('INSERT INTO student(name,age)VALUES(%s,%s)'student_lst)
mydb.commit()