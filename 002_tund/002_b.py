string_sample1= 'Hello world world'
string_sample2= 'first letteR is loWerCase'
string_sample3= '**** extra whitespace string*'
german_sample= 'der Fluß'

print(string_sample3.strip('* ')) #remove space *or symbolsat at the start and end of string
print(string_sample3.lstrip('* ')) #remove at the left
print(string_sample3.rstrip('* ')) #remove at the right
print(string_sample2.replace(' ' ,'')) #remove all spaces
print(string_sample2.lower().replace(' ' ,'')) #remove all spaces


    #a, b, c,= string_sample1.split()
     # print(a)
     # print(b)
     # print(c)

print(string_sample1.count('world'))
print(string_sample1.find('world')) #find first world in string and then stop
print('world'in string_sample1)