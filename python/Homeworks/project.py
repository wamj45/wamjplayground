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
#       Initialize values/variables to be used throughout the program
#       pass in user input as path
#       verify the path the program is running in is the same path containing images
#       if not change to the correct directory containing the images
#       Start
#           search for images of all types within path and append them to a list
#           Iterate through the list and calculate luminance for each image,
#               return relative luminance
#           Iterate through the image list once more and calculate the brightness of each image
#               return precieved brightness
#           Load data into dictiunary
#           Convert dictionary to JSON file and write to file in the directory
#       End
#
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

        for image in self.image_list:
            # Convert image to greyscale (black and white)
            img = Image.open(image).convert('L')
            stat = ImageStat.Stat(img)
            # average brightness of all pixels, returns as a list of one element
            brightness = stat.mean[0]

        return brightness

    def luminance_calculation(self):

        dir = self.get_correct_dir()

        for image in self.image_list:

            img = Image.open(image)
            stat = ImageStat.Stat(img)
            # R,G,B average values
            try:
                rgb_values = stat.mean
                r = stat.mean[0]
                g = stat.mean[1]
                b = stat.mean[2]

            except Exception as arg:
                print('{}. RGB values cannot be completely filled for [{}]'.format(str(arg), image))
            # print(f"This is the {g}")
            if r not in rgb_values:
                r = 0.0
                rgb_values.append(r)
            if g not in rgb_values:
                g = 0.0
                rgb_values.append(g)
            if b not in rgb_values:
                b = 0.0
                rgb_values.append(b)

            if len(rgb_values) > 3:
                rgb_values = rgb_values[:3]

            print(f"These are the values: {rgb_values} for image: [{image}]")
            luminance = [r,g,b]
            self.data[image] = 'luminance'
            self.data[image]['luminance'] = luminance
        return luminance

    def output(self):
         # for img in self.image_list:
         #     self.data[img] =
        if self.load_images() is False:
             print('Error - Unable to locate images files in [{}]'.format(
                self.path))
        if self.luminance_calculation() is False:
             print('Error - Unable to calculate luminance')
             return False
        if self.brightness_calculation() is False:
            print('Error - Unable to calculate brightness')
            return False

        print(self.data)
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
    if image_evaluater.output() is False:
        print('Failed to load images from [{}]'.format(user_path))
        sys.exit(255)

        # Need to add a check for incorrect path

if __name__ == '__main__':
    main()
