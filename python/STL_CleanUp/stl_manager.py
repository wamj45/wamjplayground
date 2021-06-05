# this should be the dirving script of the program
# 1. look for files in the download dir
# 2. Extract the zip
# 3. remove unnecessary files, move wanted files to a new dir and move the dir to the
#       stl path
# 4. make a folder fo the stl files and move them to the stl path

import os
import sys
import config

from cleanup import ZipFileManager, STLFileManager
from locate_files import FileFinder

class STLManager():

    def __init__(self):
        self.file = None
        self.stl_files = []
        self.zip_files = []
        self.download_path = config.get_downloads_path()

    def load_files(self):
        file_loader = FileFinder()
        files = file_loader.load_fileslist()
        self.zip_files = files[0]
        self.stl_files = files[1]
        return True

    def file_cleaner(self):
        try:
            self.load_files()
        except Exception as err:
            print("Unable to load files")
            print(str(err))
            return False

        if len(self.zip_files) != 0:
            print(f"Run the zip file manager now")
            for zip_file in self.zip_files:
                self.zip_file_manager(zip_file)
        elif len(self.stl_files) != 0:
            print("Run the stl file manager for eachfile")
            for stl_file in self.stl_files:
                self.stl_file_manager(stl_file)
        else:
            print("No files found")
            print(f"Please check [{self.download_path}] for any STL or Zip files")
            return False
        return True

    def stl_file_manager(self, stl_file):
        dir_name = input(f"Please enter the name of the new dir for: [{stl_file}]\n")
        stl_file_path = os.path.join(self.download_path, stl_file)
        manager = STLFileManager(stl_file_path, dir_name, stl_file)
        if manager.save_to_dir() is False:
            print(f"Error - Failed to move [{stl_file}] to [{stl_file_path}]")
            return False
        if manager.remove_old_file(stl_file_path) is False:
            print(f"Failed to remove [{stl_file_path}]")
            return False
        return True

    def zip_file_manager(self, zip_file):
        dir_name = input(f"Please enter the name of the new dir for: [{zip_file}]\n")
        zip_file_path = os.path.join(self.download_path, zip_file)
        manager = ZipFileManager(zip_file_path, dir_name)


        return False

def main():
    run = STLManager()
    if run.file_cleaner() is False:
        sys.exit(0)

if __name__ == '__main__':
    main()
