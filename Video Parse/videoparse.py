
'''
real time record video off of camera then parse video into individual frames
'''

'''
real time record video off of camera then parse video into individual frames
'''
import cv2
import numpy as np
import os
import time
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
    
#determine whether to use front or back camera
os_type = int (input('press 0 if you are using an iphone/mac and 1 if you are usign an android phone/windows PC '))

start = time.time() + 3
currentFrame = 0
cap = cv2.VideoCapture(os_type) 
while time.time() <= start:
    ret, frame = cap.read()
    name = './data/frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    
    currentFrame += 1
# When everything done, release the capture
cv2.destroyAllWindows()
cap.release()