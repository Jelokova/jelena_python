import pandas as pd
df=pd.read_csv('2019.csv')
#pd.set_option('display.max_columns',4)
#pd.set_option('display.max_rows',160)

#print(df.loc[df['Country or region'].str.contains('on|an')])
#print(df.loc[df['GDP per capita']<1,['Country or region','Score']])

#print(df.groupby('GDP per capita').count())
#print(df.nlargest(5,'GDP per capita'))
#print(df.nsmallest(5,'GDP per capita'))
#print(pd.concat([df.nlargest(5,'GDP per capita'),df.nsmallest(5,'GDP per capita')]))
for line in pd.read_csv('2019.csv', chunksize=5):
    print(line)
    print ('*****************')