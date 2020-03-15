import re

match = re.search(r'the phone number is ([\d-]+)', '37: the phone number is 1234-567-890')
print(match.group(1))

pattern = re.compile(r'The answer to question (\w+) is (yes|no)', re.IGNORECASE)
print(pattern.search('Naturally, the answer to question 3b is YES'))
print(pattern.search('Naturally, the answer to question 3b is YES').groups())

PATTERN = re.compile(r'([A-Z][\w\s]+).(TX|OR|OH|MI)')
TEXT ='the jackalopes are the team of Odessa,TX while the knights are native of'

print(list(PATTERN.finditer(TEXT))[0].groups())
