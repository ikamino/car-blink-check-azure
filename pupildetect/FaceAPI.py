import json
import urllib
import requests
import os
import glob
import time
import cv2
import urllib.request
import urllib.parse
import base64

from pprint import pprint
from os.path import expanduser
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'

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

currentFrame = 0
cap = cv2.VideoCapture(0) 
if currentFrame == 0:
    ret, frame = cap.read()
    name = './data/frame' + str(currentFrame) + '.jpg'
    cv2.imwrite(name, frame)

# Stop recording
cap.release()
cv2.destroyAllWindows() 

# start = time.time() + 0.5
# currentFrame = 0
# cap = cv2.VideoCapture(0) 
# #album = []
# while time.time() <= start:
#     ret, frame = cap.read()
#     name = './data/frame' + str(currentFrame) + '.jpg'
#     cv2.imwrite(name, frame)
#     currentFrame += 1
# # Stop recording
# cap.release()
# cv2.destroyAllWindows()
# currentFrame = 0




assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}
            

params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}

image_diffs = []
a = (os.listdir('./data'))
print (a)
for image in a:
    # response = requests.post(face_api_url, headers=headers, data = data, params=params)
    # data = response.json()
    # print (data)
    # face_data = data[0]
    data = open('./data/' + image , 'rb')
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
    image_diffs.append(differences)

    terms_in_diffs = len(image_diffs)
    print (image_diffs)

    # face_data = data[0]
    # faceLandmarks = (face_data['faceLandmarks'])






# for image in a:
#     # response = requests.post(face_api_url, headers=headers, params=params)
#     # data = response.json()
#     # print (data)
#     # face_data = data[0]
#     response = requests.post(face_api_url, params=params,
#                             headers=headers, json={"url": image})

#     data = response.json()
#     face_data = data[0]
#     faceLandmarks = (face_data['faceLandmarks'])


# remove_data = glob.glob("./data/*")
# for r in remove_data:
#     os.remove(r)