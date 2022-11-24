import pandas as pd
#pip install openpyxl
df=pd.read_csv('2019.csv')

df.to_excel('output.xlsx')