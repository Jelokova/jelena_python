import pandas as pd
df=pd.read_csv('2019.csv')
#pd.set_option('display.max_columns', 9)
#pd.set_option('display.max_rows', 10)
print(df)
#print(df.head()) #5 by default
print(df.tail(7))

sample = {
    'name':[1,2,3,4,5],
    'second': [6,7,8,9,10]
    }
df=pd.DataFrame(sample)
print(df)
print(df['name'])
print(type(df['name'])) #type Series