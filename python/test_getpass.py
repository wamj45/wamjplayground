# A simple Python program to demonstrate
# getpass.getpass() to read password
import getpass

try:
	password = getpass.getpass('Enter password: ')
except Exception as error:
	print('ERROR', error)
else:
	print(f'You entered: {password}')
