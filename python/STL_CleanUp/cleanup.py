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
        with zipfile.ZipFile(self.file, 'r') as zip_ref:
            zip_ref.extractall(self.current_dir)
        return True

    def erase_files(self):
        files = self.listdir(self.current_dir)
        for ext in config.REMOVABLE_EXT:
            for file in files:
                if file.endswith(ext):
                    remove_path = f"{self.current_dir}/{file}"
                    os.remove(remove_path)
        for dir in config.REMOVABLE_DIRS:
            shutil.rmtree(dir)


    def load_stl_files(self):
        stl_path = os.path.join(self.current_dir, self.filename)
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

    def file_manager(self):
        print(self.file)

        if self.extract() is False:
            print("Error - Unable to extract file")
            return False

        if self.load_stl_files() is False:
            print("Error - Unable to load STL files")
            return False

        print("Removing unnecessary files...\n")
        if self.erase_files() is False:
            print("Error - Unable to erase files")
            return False

        print(f"Your STL files are in: [{self.current_dir}/{self.filename}]")
        return True

def zip_cleanup(path):
    zip_path = path[1:-2]
    zip_file = os.path.basename(zip_path)
    return zip_file


def main():
    zip_path = input("Please enter STL zip file file:\n")
    filename = input("What whould you like to call your new STL directory:\n")
    file = zip_cleanup(zip_path)

    file_cleaner = FileCleanUp(file, filename)
    if file_cleaner.file_manager() is False:
        print("Error - please check ")
        sys.exit(255)

    print("Done!")

if __name__ == "__main__":
    main()
