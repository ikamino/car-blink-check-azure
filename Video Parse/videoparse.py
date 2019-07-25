
'''
real time record video off of camera then parse video into individual frames
clientID: a230297bd00d52a
clientSecret: 0cb3594114f3a9bb95e2271d772c5261276d9b23
'''
import cv2
import numpy as np
import os
import time
import json
import urllib.request
import urllib.parse
import base64
import time

def imgur(name):
    f = open(name, "rb")
    image_data = f.read()
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': base64.standard_b64encode(image_data), 'title': 'test'} # create a dictionary.
    request = urllib.request.Request(url="https://api.imgur.com/3/upload.json", data=urllib.parse.urlencode(data).encode("utf-8"),headers=headers)
    response = urllib.request.urlopen(request).read()
    parse = json.loads(response)
    print (parse['data']['link'])

client_id = 'a230297bd00d52a'

os_type = int (input('press 0 if you are using an mac and 1 if you are usign an windows PC '))

start = time.time() + 6
currentFrame = 0
cap = cv2.VideoCapture(os_type) 
while time.time() <= start:
    ret, frame = cap.read()
    name = './frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    imgur(name)
    os.remove(name)
    currentFrame += 1
# Stop recording
cv2.destroyAllWindows()
cap.release()
