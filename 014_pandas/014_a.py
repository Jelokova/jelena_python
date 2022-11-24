import pandas as pd
#df=pd.read_csv('2019.csv', skiprows=5) # убрать первые 5 строк
#df=pd.read_csv('2019.csv', header=3) # указать заголовок
#df=pd.read_csv('tester.csv', header=None, names=['name','date', 'town'])
df=pd.read_csv('2019.csv', nrows=5) #read first 5 from the beginning
print(df)
print(type(df))

df.#to_csv('new.csv',index=False, header=False,columns=['Country or region', 'GDP per capita']) #only two colums and 5 rows
print(df.columns)
print(type(df.columns))
