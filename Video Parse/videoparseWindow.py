'''
video parsing for PCs with Windows operation system.
Purpose: 
    video is parsed to frames and stored into a folder called 'data'
'''


import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('example.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False: 
        break
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()