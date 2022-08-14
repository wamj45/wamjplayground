import os
from config_manager import CfgManager

CFG_FILE = "keep.json"

def main():
    cfg = CfgManager(CFG_FILE)
    if cfg.initialize() is False:
        print(f"Error - Failed to Initialize Config Manager")
        os._exit(100)
    print("Done!")

if __name__ == '__main__':
    main()
