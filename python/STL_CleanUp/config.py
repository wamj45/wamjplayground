# Config file. Edit path functions to name of desired path to save/iterate through
import os

def get_downloads_path():
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")

def get_STL_path():
    home = os.path.expanduser("~")
    # Change to reflect the correct dir
    stl_path = "3D-Printing/Prints/STL-files"
    return os.path.join(home, stl_path)
