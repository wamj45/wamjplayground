import os
from config_manager import CfgManager
from file_manager import FileManager

CFG_FILE = "keep.json"

def main():
    cfg = CfgManager(CFG_FILE)
    if cfg.initialize() is False:
        print(f"Error - Failed to Initialize Config Manager")
        os._exit(100)

    file_mng = FileManager(cfg)
    if file_mng.initialize() is False:
        print("Error - Failed to Initialize File Manager!")
        os._exit(255)
    file_mng.start()
    print("Done!")

if __name__ == '__main__':
    main()
