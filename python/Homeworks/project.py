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

# Python Imaging Library(PIL) used to manipulate images in Python
from PIL import Image


class ImageEvaluator:

    def __init__(self, path):
    # Initialize values
        self.path = path
        self.image_list = []
        self.data = {}

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
                print('test')
                if jpg_type in file_type:
                    self.image_list.append(file_type)
                if JPG_type in file_type:
                    self.image_list.append(file_type)
                if jpeg_type in file_type:
                    self.image_list.append(file_type)
                if JPEG_type in file_type:
                    self.image_list.append(file_type)
                if png_type in file_type:
                    self.image_list.append(file_type)
                if PNG_type in file_type:
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

        for image in self.image_list:
            #Converts image to greyscale
            img = image.open(image).convert('L')
            stat = ImageStat.Stat(img)
            # R,G,B average values
            r = stat.mean
            g = stat.mean
            b = stat.mean
            brightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

        return True

    def luminance_calculation(self):


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
    user_path = input(path_message)

    # Calls the ImageEvaluator class and exits if cannot run
    image_evaluater = ImageEvaluator(user_path)
    if image_evaluater.brightness_calculation() is False:
        print('Failed to load images from [{}]'.format(user_path))
        sys.exit(255)

        # Need to add a check for incorrect path



if __name__ == '__main__':
    main()
