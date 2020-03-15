import re

print(re.search(r'LOG', 'LOGS'))
print(re.search(r'LOG', 'NOT A MATCH'))
print(re.search(r'LOG', 'SOME LOGS').span())

STRING = 'something in the things she shows me'

match = re.search(r'thing', STRING)
print(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():])

match = re.search(r'\bthing', STRING)
print(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():])

phone_match = re.search(r'[0123456789-]+', 'the phone number is 1234-567-890')
print(phone_match)

email_match = re.search(r'\S+@\S+', 'my email is email.123@test.com').group()
print(email_match)