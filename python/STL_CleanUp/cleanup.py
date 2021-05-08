# This will open Thingiverse zip file and will:
# 1. Extract the contents
# 2. Erase all unncessary files
# 3. mv the STL files into a dir(user will need to enter name w/o .zip)

import os
import zipfile
import config
import pathlib

class ZipFileManager():

    def __init__(self, zip_file, filename):
        self.zip_file = zip_file
        self.filename = filename
        self.current_dir = config.get_downloads_path()


    def extract(self):
        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
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

class STLFileManager():

    def __init__(self, stl_file, dirname):
        self.stl_file = stl_file
        self.new_dirname = dirname

    def create_dir(self):
        stls_path = config.get_STL_path()
        new_filepath = os.path.join(stls_path, self.new_dirname)
        os.mkdir(new_filepath)
        return new_filepath

    def save_to_dir(self):
        # Have to use the rename method
        # https://www.geeksforgeeks.org/how-to-save-file-with-file-name-from-user-using-python/
        stl_save_dir = self.create_dir()
        print(stl_save_dir)

        return True
