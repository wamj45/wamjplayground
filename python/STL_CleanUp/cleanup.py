# This will open Thingiverse zip file and will:
# 1. Extract the contents
# 2. Erase all unncessary files
# 3. mv the STL files into a dir(user will need to enter name w/o .zip)

import os
import sys
import zipfile
import config

class FileCleanUp():

    def __init__(self, file, filename):
        self.file = file
        self.filename = filename
        self.current_dir = os.getcwd()

    def extract(self):
        print(f"These are the args parsed in: [{self.file}] and [{self.filename}]")
        print(f"This is the current working dir: [{self.current_dir}]")

        with zipfile.ZipFile(self.file, 'r') as zip_ref:
            zip_ref.extractall(self.current_dir)

        return True





def main():
    # file = input("Please enter STL zip file file:\n")
    file = config.FILENAME
    filename = input("What whould you like to call your new STL file:\n")

    file_cleaner = FileCleanUp(file, filename)
    if file_cleaner.extract() is False:
        print("Error - please check ")
        sys.exit(255)

if __name__ == "__main__":
    main()
