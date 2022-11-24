import pandas as pd
import mysql.connector
conn=mysql.connector.connect (
    user=''
    password=''
    host=''
    datebase=''

)

data = pd.read_sql_query('SELECT*FROM actor',conn)
