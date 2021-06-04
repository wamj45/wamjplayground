# This will open Thingiverse zip file and will:
# 1. Extract the contents
# 2. Erase all unncessary files
# 3. mv the STL files into a dir(user will need to enter name w/o .zip)

import os
import zipfile
import config
import shutil

class ZipFileManager():

    def __init__(self, zip_file, filename):
        self.zip_file = zip_file
        self.filename = filename
        self.downloads_dir = config.get_downloads_path()


    def extract(self):
        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
            zip_ref.extractall(self.downloads_dir)
        return True

    def erase_files(self):
        files = self.listdir(self.downloads_dir)
        for ext in config.REMOVABLE_EXT:
            for file in files:
                if file.endswith(ext):
                    remove_path = f"{self.downloads_dir}/{file}"
                    os.remove(remove_path)
        for dir in config.REMOVABLE_DIRS:
            shutil.rmtree(dir)
        return True

class STLFileManager():

    def __init__(self, stl_file_path, dirname, stl_file):
        self.stl_file_path = stl_file_path
        self.new_dirname = dirname
        self.stl_file = stl_file

    def create_dir(self):
        stls_path = config.get_STL_path()
        new_filepath = os.path.join(stls_path, self.new_dirname)
        os.mkdir(new_filepath)
        return new_filepath

    def save_to_dir(self):
        stl_save_dir = self.create_dir()
        dest = os.path.join(stl_save_dir, self.stl_file)
        src = self.stl_file_path
        try:
            shutil.copyfile(src, dest)
        except OSError as e:
            print(f"Error - [{src}] [{e.strerror}]")
            return False
        return True

    def remove_old_file(self, og_file):
        try:
            os.remove(og_file)
        except OSError as e:
            print(f"Error - {og_file} {e.strerror}")
            return False
        return True
