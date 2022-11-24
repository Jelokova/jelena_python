import re

emails = '''
33
333@example
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''
#### 1
# pattern= re.compile(r'[A-Za-z-._+\d]+@[A-Za-z\d.-]+')
# matches=pattern.finditer(emails)
# for match in matches:
#     print(match)
### 2
# pattern = re.compile(r'(http://|https://)?(www\.)?([A-Za-z0-9-]+)(\.[A-Za-z0-9]+)')
# matches = pattern.finditer(urls)
# subbed_urls = pattern.sub(r'\1\2', urls)  # sub seach by group () in pattern
# print(subbed_urls)
# for match in matches:
#     print(match.group(3)+(match.group(3)) #match.group no index only results by group
# ) #match.group no index only results by group

### 3 findall retun list on matches no index. result type is list
# pattern = re.compile(r'www\.')
# matches = pattern.findall(urls)
# print(matches)

### 4 fullmatch полное совпадение
# pattern = re.compile(r'\d+')
# matches = pattern.fullmatch('45')
# print(matches)

### 5 search returns the FIRST match for a pattern in a string. The search happens from left to right.
# pattern = re.compile(r'\d+')
# matches = pattern.search(emails)
# print(matches)

### 6 match search the regular expression pattern and return the FIRST occurrence.
pattern = re.compile(r'\d+')
matches = pattern.match('33333333')
print(matches)