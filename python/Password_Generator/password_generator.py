# This script will generate a unique password for the user
# Save the password into a text or JSON file for easy readability
# User will have to pass in which site/application the generator is making the password for
# We will use the uuid4() method for this application

import os
import sys
import uuid

class PasswordManager():

    def __init__(self, site):
        self.site = site





def main():
    site = input("\nPlease enter the site/application we are generating a password for: ")
    print(f"This is the {site} we are working with")

if __name__ == "__main__":
    main()
