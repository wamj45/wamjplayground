import os
import fnmatch
import config

class FileFinder():

    def __init__(self):
        self.download_path = config.get_downloads_path()
        self.zip_files = []
        self.stl_files = []

    # Asks user which files are the ones we want to extract
    def load_fileslist(self):
        zip_pattern = "*.zip"
        self.zip_files = self.match_files(zip_pattern)
        wanted_zip_files = self.create_fileslist(self.zip_files)

        stl_pattern = "*.stl"
        self.stl_files = self.match_files(stl_pattern)
        wanted_stl_files = self.create_fileslist(self.stl_files)

        return wanted_zip_files, wanted_stl_files

    def match_files(self, pattern):
        match_files = []
        load_files = os.listdir(self.download_path)
        for file in load_files:
            if fnmatch.fnmatch(file, pattern):
                match_files.append(file)
        return match_files

    def create_fileslist(self, files):
        fileslist = []
        for file in files:
            val = input(f"Is [{file}] the file we are looking for? (y/n)\n")
            if val == "y":
                fileslist.append(file)
        return fileslist
