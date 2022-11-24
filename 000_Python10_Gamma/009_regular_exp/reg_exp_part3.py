import re

emails = '''
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
//www.nasa.gov.uk
www.example.net
example.net
'''


# # Emails #
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')  # Let's make our own pattern
#
# matches = pattern.finditer(emails)
# for match in matches:
#     print(match)

# URLs #
# pattern = re.compile(r'https?://(www\.)?(\w|-)+\.\w+')
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')  # Ungrouped pattern
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # Grouped pattern


# # # Subbed pattern #
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)

pattern=re.compile(r'(http://|https://)?(www\.)?([A-Za-z0-9-]+)(\.[A-Za-z0-9]+)')
matches = pattern.finditer(urls)
subbed_urls = pattern.sub(r'\1\2', urls) #sub seach by group () in pattern
print(subbed_urls)
#
# for match in matches:
#     print(match)
    # print(match.group(0))  # Group 0 is entire match
    # print(match.group(1))  # Numbers stand for group number
    # print(match.group(2)+match.group(3))  # Can be added to each other

