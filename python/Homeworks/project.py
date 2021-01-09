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

# Python Imaging Library(PIL) used to manipulate images in Python
from PIL import Image
from PIL import ImageStat

class ImageEvaluator:

    def __init__(self, path):
    # Initialize values
        self.path = path
        self.image_list = []
        self.data = []
        self.img_dict = None
        self.luminance_dict = {}
        self.brightness_dict = {}

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

    def luminance_calculation(self):
        # Calculates the relative luminance and the brightness of an image

        # Gets the correct containing the images first
        dir = self.get_correct_dir()

        for image in self.image_list:
            img = Image.open(image)
            stat = ImageStat.Stat(img)
            grey_img = img.convert('L')
            grey_stat = ImageStat.Stat(grey_img)
            # R,G,B average values, if any value is None, will continue to iterate
            try:
                rgb_values = stat.mean
                r = stat.mean[0]
                g = stat.mean[1]
                b = stat.mean[2]
                brightness = grey_stat.mean[0]
                brightness = '{:.2f}'.format(brightness)
            except Exception as arg:
                print('{}. Missing RGB values will be passed in as 0.0 for [{}]'.format(str(arg), image))
            # If missing a value for R,G, and/or B then 0.0 will be set for missing value
            if r not in rgb_values:
                r = 0.0
                rgb_values.append(r)
            if g not in rgb_values:
                g = 0.0
                rgb_values.append(g)
            if b not in rgb_values:
                b = 0.0
                rgb_values.append(b)

            # Ignores the RGBA format, which is utilized by default
            if len(rgb_values) > 3:
                rgb_values = rgb_values[:3]

            r_value = 'Red: {:.2f}'.format(r)
            g_value = 'Green: {:.2f}'.format(g)
            b_value = 'Blue: {:.2f}'.format(b)

            # Calculation of luminance
            luminance = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
            luminance = '{:.2f}'.format(luminance)

            # Populating dictionary for each image
            self.img_dict = {'Image': image}
            self.img_dict['RBG Values'] = [r_value, g_value, b_value]
            self.img_dict['Luminance'] = luminance
            self.img_dict['Brightness'] = brightness

            self.data.append(self.img_dict)
        return True

    def output(self):
        # Program starts here
        if self.load_images() is False:
             print('Error - Unable to locate images files in [{}]'.format(
                self.path))
        if self.luminance_calculation() is False:
             print('Error - Unable to calculate luminance')
             return False
        # Writes output to a JSON file
        with open("data.json", "w") as data_file:
            json.dump(self.data, data_file)

        return True
def main():

    # Asks user to enter dir containing images
    path_message = 'Please enter the directory/folder containing the images: '
    # user_path = input(path_message)
    user_path = input(path_message)
    # Calls the ImageEvaluator class and exits if cannot run
    image_evaluater = ImageEvaluator(user_path)
    if image_evaluater.output() is False:
        print('Failed to load images from [{}]'.format(user_path))
        sys.exit(255)
    else:
        print('Done!')
        print('Look in [{}] for output file'.format(user_path))

if __name__ == '__main__':
    main()
