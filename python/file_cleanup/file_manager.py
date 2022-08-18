import os, zipfile, shutil
from pathlib import Path

class FileManager:
    def __init__(self, config):
        self.config_manager    = config
        self.cfg               = None
        self.temp_dir          = None
        self.target_dir        = None

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
        self.target_dir = self.move_target()

        self.temp_dir = self.create_temp_dir()
        # extract target
        if self.temp_dir is False or self.target_dir is False:
            return False

        self.extract_files(self.temp_dir, self.target_dir)

        if self.make_dirs() is False:
            return False

        # sort files from target
        self.sort_files()
        # create new dirs for the extensions to hold files

        return True

    def move_target(self):
        src_path = f"{self.cfg['target_path']}/{self.cfg['target_dir']}"
        dest_path = f"{os.getcwd()}/files.zip"
        try:
            print(f"Moving {self.cfg['target_dir']} to local path...")
            Path(src_path).rename(dest_path)
            return dest_path
        except Exception as e:
            print(f"Error \n{str(e)}")
            os._exit(1)
            return False


    def create_temp_dir(self):
        temp_dir = f"{os.getcwd()}/temp"
        try:
            print("Creating temporary directory to hold files...")
            os.mkdir(temp_dir)
            return temp_dir
        except OSError as e:
            print("Temp dir already exists")
            return temp_dir
        except Exception as err:
            print(f"Error Failed to create temporary directory\n{str(err)}")
            return False

    def extract_files(self, dest, src):
        print("Extracting files to temp dir...")
        with zipfile.ZipFile(src, "r") as zip_src:
            zip_src.extractall(dest)
        return

    def make_dirs(self):
        things = self.cfg.get("keep_things")
        keep_files = things.get("files")
        keep_types = things.get("extensions")
        dirs = list(keep_types.keys())

        for ext in dirs:
            path = f"{os.getcwd()}/{ext}"
            print(f"Creating {ext} dir...")
            try:
                os.mkdir(path)
            except OSError as os_e:
                print(f"{path} Already exists")
            except Exception as e:
                print(f"Error - Failed to Create [{path}]\n{str(e)}")
                return False
        return True

    def sort_files(self):

        return
