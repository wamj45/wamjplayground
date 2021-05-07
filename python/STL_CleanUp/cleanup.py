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
