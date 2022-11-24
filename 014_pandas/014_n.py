import pandas as pd
df=pd.read_csv('2019.csv')
pd.set_option('display.max_columns',9)
df.insert(loc=3,column='New Column',value=(df['GDP per capita']*10)) #add colimn to ind 3
print(df)
print(df.dtypes)


