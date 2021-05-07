# this should be the dirving script of the program
# 1. look for files in the download dir
# 2. Extract the zip
# 3. remove unnecessary files, move wanted files to a new dir and move the dir to the
#       stl path
# 4. make a folder fo the stl files and move them to the stl path

import os
import sys
from locate_files import FileFinder
import cleanup
import config

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

        if len(self.stl_files) == 0 and len(self.zip_files) == 0:
            print("No files found")
            print(f"Please check [{self.download_path}] for any STL or Zip files")
            return False

        return True

def main():
    run = STLManager()
    if run.load_files() is False:
        sys.exit(0)

if __name__ == '__main__':
    main()
