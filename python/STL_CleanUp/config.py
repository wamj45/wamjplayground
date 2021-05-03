# Config file. Edit path functions to name of desired path to save/iterate through

import os

FILENAME = "Micro_SD_card_and_adapter_storage_box_.zip"
REMOVABLE_EXT = [".txt", ".html", ".zip"]
REMOVABLE_DIRS = ["files", "images"]


def get_downloads_path():
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")
