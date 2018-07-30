import re

validation = re.compile(r'[\w+]@[A-Za-z]+\.["com" | "org" | "edu" | "net"]')

email = input('Please enter your email: ')

while not validation.search(email):
    print('Please enter your email correctly!')
    email = input('Please enter your email: ')

print('\nYour email is {}!'.format(email))
