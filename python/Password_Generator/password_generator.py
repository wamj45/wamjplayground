# This script will generate a unique password for the user
# Save the password into a text or JSON file for easy readability
# User will have to pass in which site/application the generator is making the password for
# We will use the uuid4() method for this application

import os
import sys
import uuid

class PasswordManager():

    def __init__(self, site, note):
        self.site = site
        self.note = note
        self.password_file = "PasswordManager.txt"

    def create_password(self):
        return password

    def create_txt_file(self, file):
        create_file = open(file, "w+")
        create_file.close()
        return create_file

    def write_txt_file(self):
        try:
            self.open_txt_file(self.password_file)
        except Exception as arg:
            print(f"Error - No {self.password_file} found" + str(arg))
            print(f"Creating the Password Manager file in this dir...")

            self.create_txt_file(self.password_file)
        
        return True

    def open_txt_file(self, file):
        f = open(file, "r")
        return f

def main():
    site = input("Please enter the site/application we are generating a password for: ")
    note = input("\nPlease enter a quick note about this password: ")

    passwordmanager = PasswordManager(site, note)
    if passwordmanager.write_txt_file() is False:
        print("Error - Unable to open/create the text file for password")
        sys.exit(255)

if __name__ == "__main__":
    main()
