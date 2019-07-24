import requests
import json
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

image_url = 'https://media.discordapp.net/attachments/413154933278507008/603272127176507392/20190723_100743.jpg?width=681&height=908'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true'  
}



response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})



data = response.json()

face_data = data[0]
faceLandmarks = (face_data['faceLandmarks'])

#print (faceLandmarks)

pupilLeft = faceLandmarks['pupilLeft']
pupilRight = faceLandmarks['pupilRight']
print ("Pupil Left:", pupilLeft)
print ("Pupil Right:", pupilRight)

