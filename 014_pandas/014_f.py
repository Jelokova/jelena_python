import pandas as pd
df=pd.read_csv('2019.csv')

for index, row in df.iterrows():
    print (index,row)
    print(row['Country or region'])