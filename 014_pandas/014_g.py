import pandas as pd
df=pd.read_csv('2019.csv')
print(df.loc[df['Country or region']=='Estonia'])
print(df.loc[df['GDP per capita']>1])
print(df.describe())
print(df.memory_usage(deep=True)) #to see memory usage

print(df.sort_values('Country or region',ascending=False)) #sorting by column
df['Total'] = (df['GDP per capita']+df['Generosity'])**2 #create new column
print(df)

print(df['Total'])
df2=df.drop(columns=['Total'])
print(df2)