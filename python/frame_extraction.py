import cv2
import os
import time
import progressbar
#ToDo:
# Need to add a progress bar to this and the ability to click and drag file location
# fix the prgress bar to only show up once
# printout the total amount of images created
# May have to write this in OOP for clarity for myself
# for the click and drag feature you can remove the quotations from the input
class ImageCreator:
    vid_folder = input('Enter the folder containing the videos: ')
    img_folder = input('Enter the folder which will contain the images: ')
    listing = os.listdir(vid_folder)

    count=1

    for vid in listing:
        vid = vid_folder + vid
        vidcap = cv2.VideoCapture(vid)

        def getFrame(sec):
            bar = progressbar.ProgressBar()
            for i in bar(range(100)):
                vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
                hasFrames,image = vidcap.read()
                if hasFrames:
                    cv2.imwrite(img_folder + str(count)+".jpg", image) # Save frame as JPG file
                time.sleep(0.02)
            return hasFrames

        sec = 0
        frameRate = 2 # Change this number to 1 for each 1 second

        success = getFrame(sec)

        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = getFrame(sec)

def main():

    image_creator = ImageCreator()
    

if __name__ == '__main__':
    main()
