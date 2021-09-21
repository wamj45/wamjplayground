# This script will generate a unique password for the user
# Save the password into a text or JSON file for easy readability
# User will have to pass in which site/application the generator is making the password for
# We will use the uuid4() method for this application

import os
import sys
import uuid
import json

class PasswordManager():

    def __init__(self, site, note):
        self.site = site
        self.note = note
        self.password_file = "PasswordManager.txt"

    def writeToFile(self):
        try:
            password = self.generate_password()
            # outputString = f"Site: {self.site}\tNote: {self.note}\tPassword: {self.generate_password()}"
            outputDict = dict({self.site : password})
            f = self.open_txt_file(self.password_file)
            f.write(json.dumps(outputDict))
            f.close()
            print(f"Successfully created password for {self.site}")
        except Exception as arg:
            print(str(arg))
            print("Exiting...")
            sys.exit(255)
        return True

    def open_txt_file(self, file):
        f = open(file, "a")
        return f

    def read_txt_file(self, file):
        f = open(file, "r")
        return f

    def generate_password(self):
        generate = str(uuid.uuid4())
        password = generate.replace("-", "")
        return password

    # Verify site provided does not already have a password existing
    # Convert ouptut to a JSON file that way we only have to search for the key as the Site

    def passwordCheck(self):
        f = self.read_txt_file(self.password_file)
        for line in f:
            print(line)

        pass

def main():
    site = input("Please enter the site/application we are generating a password for: ")
    note = input("\nPlease enter a quick note about this password: ")

    passwordmanager = PasswordManager(site, note)
    if passwordmanager.writeToFile() is False:
        print("Error - Unable to open/create the text file for password")
        sys.exit(255)
    print("Done!")
    sys.exit(0)

if __name__ == "__main__":
    main()
