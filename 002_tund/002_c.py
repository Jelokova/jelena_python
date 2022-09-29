salary = 2000
sample_string = 'John salary is {1},{2},{0}'
print(sample_string.format(salary,'one','two'))

price_string ='This {product:} costs {price:2f} USD'
print (price_string.format (product='computer', price=1234))

name='jack'
surname = 'smith'
age='20'

print(f'Hello {name.capitalize()} {surname}.You are {age} years old.Your salary is {salary:2f} EUR.')
print('That\'s it')
print ('Hello \nwor\tld')
