# this should be the dirving script of the program
# 1. look for files in the download dir
# 2. Extract the zip
# 3. remove unnecessary files, move wanted files to a new dir and move the dir to the
#       stl path
# 4. make a folder fo the stl files and move them to the stl path

import os
import sys
import locate_files
import cleanup
import config
