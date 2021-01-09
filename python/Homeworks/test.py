# import sys
# import os
# import fnmatch
# import re
#
# from PIL import Image
#
#
# image_list = []
# FILENAME_REGEX = '[0-9,A-Z,_-]+'
# jpg = '*.jpg'
# # need to filx this call fofr the regex
#
# def load_images(path):
#
#     for root, dirs, files in os.walk(path):
#         for file_type in files:
#             if fnmatch.fnmatch(file_type, jpg):
#                 image_list.append(file_type)
#
#     return image_list
#
# def brightness_calculation():
#     images = load_images()
#     print('Called')
#     for img in image_list:
#         re_ret = re.search(FILENAME_REGEX, img)
#         base_img_filename = re_ret.group(0)
#         img_filename = '{}.jpg'.format(base_img_filename)
#
#     return img_filename
#
# user_path = '/home/wamj/Pictures/Pics/'
#
# image_evaluater = load_images(user_path)

list = [
    'Hi',
    "you",
    "test"
]

print(list)
