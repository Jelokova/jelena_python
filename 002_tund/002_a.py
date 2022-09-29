string_sample1= 'Hello world world'
                #01234567
                #       -7-6-5-4-3-2-1
string_sample2= 'first letteR is loWerCase'
string_sample3= ' extra whitespace string'
german_sample= 'der Fluß'

a= """funny 
cats"""
print(a)

print (len(str(2232141)))
print (len(string_sample1))
print(string_sample1[1])
####print(string_sample1[len(string_sample1-1)])
#[start:end:step]
print(string_sample1[0:5])#symbols 1-4 5 is excluded
print (string_sample1[-5:])
print (string_sample1[0:10:2])
print (string_sample1[::-1]) #string otherwice

print(string_sample1.upper())
print(german_sample.lower())
print(german_sample.casefold())
print('STRING'.isupper())

print(string_sample2.capitalize()) #caps letter for first world in string *NB!not sentances
print(string_sample2.title()) #every world with upper
print(string_sample2.istitle())