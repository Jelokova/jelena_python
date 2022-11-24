import pandas as pd
df=pd.read_csv('2019.csv')
print(df.shape)
print(df['Country or region']. value_counts()) #count in coilum
data=df.loc[2]
print(data['Country or region']+' '+str(data['Social support']))
