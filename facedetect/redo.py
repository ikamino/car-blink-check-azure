import requests
import json
import cv2
import numpy as np
import os
import time
import urllib.request
import urllib.parse
import base64
import time
import sys
import glob
import winsound
import tkinter as tk
subscription_key = 'fc9c9a47ba614db49c896d82a6d28282'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}
params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}

threshold = 5

def soundAlert():
    duration = 1000
    freq = 440
    winsound.Beep(freq,duration)

def checkAsleep():
    data = open('./data2/temp.jpg', 'rb')
    response = requests.post(face_api_url, params=params,
                            headers=headers, data = data)

    b = response.json()

    face_data = b[0]
    faceLandmarks = (face_data['faceLandmarks'])

    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']

    y1 = (eyeLeftTop['y'])
    y2 = (eyeLeftBottom['y'])

    differences = y2-y1

    if differences > threshold:
        return False
    else:
        return True

image_diffs = []

def main():

    if os.path.exists('data2') == True:
            remove_data = glob.glob("./data2/*")
            for r in remove_data:
                os.remove(r)
    else:
        try:
            if not os.path.exists('data2'):
                os.makedirs('data2')
        except OSError:
            print ('Error: Creating directory of data')

    cap = cv2.VideoCapture(0) 

    startTime = time.time()

    lastEyesClosed = False
    eyesClosed = False
    eyesClosedCount = 0

    while(cap.isOpened()):
        ret, frame = cap.read()

        currentTime = time.time()
        if (currentTime - startTime > 3):
            cv2.imwrite('./data2/temp.jpg', frame)

            # Do diff check here
            eyesClosed = checkAsleep()
            if eyesClosed == True:
                eyesClosedCount += 1
            else:
                eyesClosedCount = 0

            if (eyesClosedCount > 1):
                soundAlert()

            startTime = currentTime

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop recording
    cap.release()
    cv2.destroyAllWindows() 

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text = "Start", 
                   fg="red", 
                   command=main
                   )
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, 
                   text = "Quit",
                   command = quit)
slogan.pack(side=tk.RIGHT)
root.mainloop()