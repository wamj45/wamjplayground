#**********************  project.py  *********************
#
# Name: Wilbert Acosta Martinez Jr
#
# Course: CSCI 1470
#
# Assignment: CSCI Python Project
#
# Algorithm:
#   Prompt user to enter the directory to search for images
#   call ImageEvaluator
#       pass in user input as path
#       search for images within path and append them to a list
#       Iterate through the list and calculate brightness and luminance for each image
# **********************************************************

import os
import json
import sys
import math
import fnmatch
import re

# Python Imaging Library(PIL) used to manipulate images in Python
from PIL import Image
from PIL import ImageStat

FILENAME_REGEX = '[0-9,A-Z,_-]+'

class ImageEvaluator:

    def __init__(self, path):
    # Initialize values
        self.path = path
        self.image_list = []
        self.data = {}
    # Changes the dir to the path containing images
    def get_correct_dir(self):
        current_dir = os.getcwd()
        if current_dir == self.path:
            return self.path
        else:
            correct_dir = os.chdir(self.path)
            return correct_dir

    def load_images(self):
    # Loads images into the image list. If no images found, exits program with error message
        jpg_type = '*.jpg'
        JPG_type = '*.JPG'
        jpeg_type = '*.jpeg'
        JPEG_type = '*.JPEG'
        png_type = '*.png'
        PNG_type = '*.PNG'

        for root, dirs, files in os.walk(self.path):
            if not files:
                print('Error - There are no files in this directory')
                return False

            for file_type in files:
                # print('test')
                if fnmatch.fnmatch(file_type, jpg_type):
                    self.image_list.append(file_type)
                elif fnmatch.fnmatch(file_type, JPG_type):
                    self.image_list.append(file_type)
                elif fnmatch.fnmatch(file_type, jpeg_type):
                    self.image_list.append(file_type)
                elif fnmatch.fnmatch(file_type, JPEG_type):
                    self.image_list.append(file_type)
                elif fnmatch.fnmatch(file_type, png_type):
                    self.image_list.append(file_type)
                elif fnmatch.fnmatch(file_type, PNG_type):
                    self.image_list.append(file_type)
                else:
                    print('Error - Unable to locate any image files in [{}]. Please try a diffent file path.'
                        .format(self.path))
                    return False

        return True

    def brightness_calculation(self):
    # Calculates the brightness of an image. Returns as a precieved brightness of image
        if self.load_images() is False:
            print('Error - Unable to begin brightess calculation')
            return False

        dir = self.get_correct_dir()

        for image in self.image_list:
            # Convert image to greyscale (black and white)
            img = Image.open(image).convert('L')
            stat = ImageStat.Stat(img)
            # average brightness of all pixels, returns as a list of one element
            brightness = stat.mean[0]
            print('[{}] has a brightness of: [{}]'.format(image, brightness))

            # Todo:
            # Add to dictionary the brightess level of each image
            # self.data[image] = brightness

        return True

    def luminance_calculation(self):

        dir = self.get_correct_dir()

        for image in self.image_list:
            # print(image)
            img = Image.open(image)
            stat = ImageStat.Stat(img)
            # R,G,B average values
            rgb_values = stat.mean
            r = stat.mean[0]
            g = stat.mean[1]
            b = stat.mean[2]

            # Todo:
            # Call this method
            # Add a check
            # Add to the dictionary the calues of relative luminance

        return True

    def output(self):
         # for img in self.image_list:
         #     self.data[img] =
        return True
def main():
    # This is kind of annoying to type everytime.
    # May have to add a click and drag into terminal
    # Asks user to enter dir containing images
    path_message = 'Please enter the directory/folder containing the images: '
    # user_path = input(path_message)
    user_path = '/home/wamj/Pictures/Pics/'
    # Calls the ImageEvaluator class and exits if cannot run
    image_evaluater = ImageEvaluator(user_path)
    if image_evaluater.brightness_calculation() is False:
        print('Failed to load images from [{}]'.format(user_path))
        sys.exit(255)

        # Need to add a check for incorrect path



if __name__ == '__main__':
    main()
