'''
A simple Python program to demonstrate
#getpass.getpass() to read password
'''

import getpass, os

try:
	password = getpass.getpass('Enter password: ')
except Exception as error:
	print(f"Failed to set password:\n{str(error)}")
else:
	print(f'You entered: {password}')
	os._exit(0)

