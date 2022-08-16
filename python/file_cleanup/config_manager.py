# Load the keep.json file
import json

class CfgManager:
    def __init__(self, config_file):
        self.cfg_file   = config_file
        self.config     = None

    def initialize(self):
        try:
            with open(self.cfg_file) as cfg_file:
                self.config = json.load(cfg_file)
            cfg_file.close()
        except FileNotFoundError as ferr:
            print(f"Error: [{self.cfg_file}] NOT found! Please verify file")
            return False
        return True

    def load_config(self):
        return self.config
