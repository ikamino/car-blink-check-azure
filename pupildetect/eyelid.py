import requests
import json
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


control = ['https://cdn.discordapp.com/attachments/413154933278507008/603370106558611456/20190723_163111_HDR.jpg']
images = ['https://cdn.discordapp.com/attachments/413154933278507008/603370106558611456/20190723_163111_HDR.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603370088325971988/20190723_163114_HDR.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603370087247773706/20190723_163116_HDR.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603370044008955924/20190723_163117_HDR.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603370042884620289/20190723_163119_HDR.jpg']
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
custom_control = (control_value - 10)
for b in range (i, terms_in_diffs):
    if image_diffs[place] < (custom_control):
        closed_times.append('closed')
        place += 1

    elif image_diffs[place] >= custom_control:
        test.append('open')
        del (closed_times[0:len(closed_times)])
        place += 1


print (image_diffs)
print (test)
