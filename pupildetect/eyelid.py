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
subscription_key = 'fc9c9a47ba614db49c896d82a6d28282'
assert subscription_key

def imgur(name):
    f = open(name, "rb")
    image_data = f.read()
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': base64.standard_b64encode(image_data), 'title': 'test'} # create a dictionary.
    request = urllib.request.Request(url="https://api.imgur.com/3/upload.json", data=urllib.parse.urlencode(data).encode("utf-8"),headers=headers)
    response = urllib.request.urlopen(request).read()
    parse = json.loads(response)
    parse2 = (parse['data']['link'])
    return parse2


client_id = 'a230297bd00d52a'


print('Please open your eyes and look at the camera')
control = []

control_frame = 0
cap = cv2.VideoCapture(0) 

if control_frame == 0:
    ret, frame = cap.read()
    control_name = './frame' + str(control_frame) + '.png'
    print ('Creating...' + control_name)
    cv2.imwrite(control_name, frame)
    imgur(control_name)
    url_control = (imgur(control_name))
    control.append(url_control)
    os.remove(control_name)
    control_frame += 1

print ('Calibration complete.')
a = input('Continue? (y/n)')
if a == 'y':
    start = time.time() + 30
    currentFrame = 0
    cap = cv2.VideoCapture(0) 
    album = []
    while time.time() <= start:
        ret, frame = cap.read()
        name = './frame' + str(currentFrame) + '.png'
        #print ('Creating...' + name)
        cv2.imwrite(name, frame)
        url_return = imgur(name)
        #print (url_return)
        album.append(url_return)
        #print (album)
        os.remove(name)
        currentFrame += 1
    # Stop recording
    cv2.destroyAllWindows()
    cap.release()
else:
    sys.exit()

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


images = album
headers = {'Ocp-Apim-Subscription-Key': subscription_key}



params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}

# imgur to azure
# imgurResp = request.post("imgururl", data={"image": file.read(path)})
# request.post("azureurl", data={"url": imgurResp.json()["url"]})
image_diffs = []
for image in control:

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})



    data = response.json()
    face_data = data[0]
    # print (data)
    faceLandmarks = (face_data['faceLandmarks'])



    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']

   

    y1 = (eyeLeftTop['y'])
    y2 = (eyeLeftBottom['y'])

    control_value = y2-y1
    image_diffs.append(control_value)
   
for image in images: 
    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})

    data = response.json()
    face_data = data[0]
    faceLandmarks = (face_data['faceLandmarks'])

    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']

    y1 = (eyeLeftTop['y'])
    y2 = (eyeLeftBottom['y'])

    differences = y2-y1
    image_diffs.append(differences)

    terms_in_diffs = len(image_diffs)


# print('Open Values: ', open_list)
# print('Close List: ' , close_list)

# #number of terms in each list
# count_open_list = len(open_list) 
# count_close_list = len(close_list)

# print("\n \n")
# print('There are ', count_open_list, ' terms in the open list.')
# print('There are ', count_close_list, ' terms in the close list.')


i = 0
place = 0
closed_times = []
test = []
custom_control = (control_value / 2)
for b in range (i, terms_in_diffs):
    if image_diffs[place] < (custom_control):
        closed_times.append('closed')
        if len(closed_times) >= 3:
            print('\a')
            break
        place += 1

    elif image_diffs[place] >= custom_control:
        test.append('open')
        del (closed_times[0:len(closed_times)])
        place += 1
    


print (image_diffs)
print (len(test), "open values")

