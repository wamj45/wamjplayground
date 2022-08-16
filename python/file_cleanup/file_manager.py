import os, zipfile, shutil
from pathlib import Path

class FileManager:
    def __init__(self, config):
        self.config_manager    = config
        self.cfg               = None

    def initialize(self):
        try:
            self.cfg = self.config_manager.load_config()
            print("Config Sucessfully Loaded...")
        except Exception as e:
            print(f"Error - Failed to load Config Data from [{self.config_manager.cfg_file}]")
            return False
        return True

    def start(self):
        # move target to current dir
        src_path = f"{self.cfg['target_path']}/{self.cfg['target_dir']}"
        dest_path = f"{os.getcwd()}/files.zip"
        try:
            Path(src_path).rename(dest_path)
        except Exception as e:
            print(f"Error \n{str(e)}")
            os._exit(1)

        temp = self.create_temp_dir()
        # extract target
        self.extract_files(temp, dest_path)
        # sort files from target
        # create new dirs for the extensions to hold files

        return

    def create_temp_dir(self):
        temp_dir = f"{os.getcwd()}/temp"
        try:
            os.mkdir(temp_dir)
            return temp_dir
        except OSError as e:
            return temp_dir
        except Exception as err:
            print(f"Error Failed to create temporary directory\n{str(err)}")
            return False

    def extract_files(self, dest, src):
        with zipfile.ZipFile(src, "r") as zip_src:
            zip_src.extractall(dest)
        return
