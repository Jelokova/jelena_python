import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
hall mall tall wall bal soul
'''

#pattern=re.compile(r'[^w]all')
# pattern=re.compile(r'\d{3}-5{3}-\d{3}')
#pattern=re.compile(r'\d{3,5}')
#pattern=re.compile(r'[abcde]{3,5}')

pattern=re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)

