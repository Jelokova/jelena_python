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
'''

sentence = 'Start a sentence and then bring it to an end'

#print(r'\tTab') #сырая строка
#attern=re.compile(r'abc')
#pattern=re.compile(r'\.')
#pattern=re.compile(r'example\.com')
#pattern=re.compile(r'\s')
#pattern=re.compile(r'\bHa') #в начале слова
#pattern=re.compile(r'Ha\b')#в конце слова
#pattern=re.compile(r'\bHa\b')#в середине слова
#pattern=re.compile(r'\BHa')#не в начале слова
#pattern=re.compile(r'^Start')#в начале строки как типа данных
#pattern=re.compile(r'\d\d\d')# три цифры подряд
#pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d.')# три цифры подряд
#pattern=re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d')# три цифры подряд между .-
#pattern=re.compile(r'[89]00.\d\d\d.\d\d\d')# начало 8 или 9 и 00
#pattern=re.compile(r'[2-5]') # диапазон от 2 до 5  и - между это диапазон
#pattern=re.compile(r'[F-M]') # диапазон от F до M  и - между это диапазон
pattern=re.compile(r'[A-Zaz]')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)
    # print(match.start())
    # print(match.end())
    # print(match.group())
    # print(match.span())
