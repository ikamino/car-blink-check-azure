
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


start = time.time() + 3
#start2 = start + 12
currentFrame = 0
cap = cv2.VideoCapture(0) 
while time.time() <= start:
    ret, frame = cap.read()
    name = './data/frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    
    currentFrame += 1
# When everything done, release the capture
cv2.destroyAllWindows()
cap.release()
#cv2.destroyAllWindows()