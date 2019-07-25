'''
THIS IS THE FINAL CODE FOR THE PROJECT
CODE FOR ALARM: 
    import winsound 
    duration = 1000
    freq = 440
    winsound.Beep(freq, duration)
    print ('\007') OR print('\a')
'''




import requests
import cv2
import numpy as np
import os
import time
import json
import urllib.request
import urllib.parse
import base64
import glob

subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

if os.path.exists('data') == True:
        remove_data = glob.glob("./data/*")
        for r in remove_data:
            os.remove(r)
else:
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Creating directory of data')
        
    

start = time.time() + 6
currentFrame = 0
cap = cv2.VideoCapture(0) 
#album = []
while time.time() <= start:
    ret, frame = cap.read()
    name = './data/frame' + str(currentFrame) + '.png'
    cv2.imwrite(name, frame)
    currentFrame += 1
# Stop recording
cap.release()
cv2.destroyAllWindows()
currentFrame = 0

print (os.listdir('./data'))
remove_data = glob.glob("./data/*")
for r in remove_data:
    os.remove(r)