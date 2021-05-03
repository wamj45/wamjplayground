import os
import sys
import fnmatch
import config

class FileFinder():

    def __init__(self):
        self.file = None
        self.download_path = config.get_downloads_path()
        self.zip_files = []
        self.stl_files = []

    def locate_zipfiles(self):
        pattern = "*.zip"
        self.zip_files = self.match_files(pattern)
        # at this point we have a list of ALL zip files in the dir
        for file in self.zip_files:

        return self.zip_files

    def locate_stl_files(self):
        pattern = "*.stl"
        self.stl_files = self.match_files(pattern)
        return self.stl_files

    def match_files(self, pattern):
        match_files = []
        load_files = os.listdir(self.download_path)
        for file in load_files:
            if fnmatch.fnmatch(file, pattern):
                match_files.append(file)
        return match_files






def main():
    files_manager = FileFinder()
    if files_manager.locate_zipfiles() is False:
        print("Error - Unable to locate downloads dir")
        sys.exit(0)
    print(files_manager.locate_zipfiles())

if __name__ == "__main__":
    main()
