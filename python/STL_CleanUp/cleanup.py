# This will open Thingiverse zip file and will:
# 1. Extract the contents
# 2. Erase all unncessary files
# 3. mv the STL files into a dir(user will need to enter name w/o .zip)

import os
import sys
import zipfile
import config
import shutil

class FileCleanUp():

    def __init__(self, file, filename):
        self.file = file
        self.filename = filename
        self.current_dir = os.getcwd()

    def listdir(self, path):
        files = []
        for file in os.listdir(path):
            files.append(file)
        return files


    def extract(self):
        print(f"These are the args parsed in: [{self.file}] and [{self.filename}]")
        print(f"This is the current working dir: [{self.current_dir}]")

        with zipfile.ZipFile(self.file, 'r') as zip_ref:
            zip_ref.extractall(self.current_dir)

        return True

    def erase_files(self):
        # if self.extract() is False:
        #     print("Error")
        #     return False
        files = self.listdir(self.current_dir)
        for ext in config.REMOVABLE_EXT:
            for file in files:
                if file.endswith(ext):
                    remove_path = f"{self.current_dir}/{file}"
                    os.remove(remove_path)
        for dir in config.REMOVABLE_DIRS:
            os.remove(dir)

        return True

    def load_stl_files(self):
        new_stl_dir = self.filename
        stl_path = os.path.join(self.current_dir, new_stl_dir)
        os.mkdir(stl_path)

        files = self.listdir(self.current_dir)
        stl_dir = "files"
        if stl_dir in files:
            stl_files = self.listdir(stl_dir)
            for stl in stl_files:
                source_path = f"{self.current_dir}/files/{stl}"
                destination_path = f"{stl_path}/{stl}"
                move = shutil.move(source_path, destination_path)

        return True





def main():
    # file = input("Please enter STL zip file file:\n")
    file = config.FILENAME
    filename = input("What whould you like to call your new STL directory:\n")

    file_cleaner = FileCleanUp(file, filename)
    if file_cleaner.load_stl_files() is False:
        print("Error - please check ")
        sys.exit(255)

if __name__ == "__main__":
    main()
