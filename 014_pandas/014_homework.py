import pandas as pd
df=pd.read_csv('survey_results_public.csv')
#выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
print('***** 1 ****')
print(df['Hobbyist'].value_counts())

print('***** 2 ****')
#2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
print('Min age =',int(df['Age'].min()))
print('Max age =',int(df['Age'].max()))
print('Average age =',int(df['Age'].mean()))

print('***** 3 ****')
#3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.
print(df['Country'].value_counts(sort=True))
#print(df.sort_values('Country or region',ascending=False)) #sorting by column

#4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания
print('***** 4 ****')
print(df['CurrencyDesc'].value_counts(sort=True))

