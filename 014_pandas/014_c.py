import pandas as pd
df=pd.read_csv('2019.csv')
print(df[['Score','Country or region']])

print(df.iloc[3:8]) # iloc for work with indexes
print(df.iloc[[1,3,6,1],3]) #rows, colums
print(df.iloc[4,3])
print(df.iloc[4, 4:9])
print(df.loc[[1,2,3,4],'Country or region':'Social support']) # c именами столбцов
print(df.loc[[1,2,3,4],['Country or region','Social support']])