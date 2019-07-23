import requests
import json
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

images = ['https://cdn.discordapp.com/attachments/413154933278507008/603272125884923947/20190723_100739.jpg','https://media.discordapp.net/attachments/413154933278507008/603272127176507392/20190723_100743.jpg?width=681&height=908']
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true'  
}


for image in images:

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})



    data = response.json()

    face_data = data[0]
    faceLandmarks = (face_data['faceLandmarks'])

    #print (faceLandmarks)
   
    #use classifier (SciKit Learn)
    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']

    print ("Eye Left Top:", eyeLeftTop, "Eye Left Bottom:", eyeLeftBottom)

    #can we use occulsion on pupils?

