import requests
import json
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

images = ['https://cdn.discordapp.com/attachments/413154933278507008/603298808495079424/20190723_114654.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603298809493192776/20190723_114701_HDR.jpg']
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true'
    # 'returnFaceAttributes': 'occlusion'  
}


for image in images:

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})



    data = response.json()
    print (data)
    face_data = data[0]
    faceLandmarks = (face_data['faceLandmarks'])

    #print (faceLandmarks)
   
    #use classifier (SciKit Learn)
    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']
    eyeRightTop = faceLandmarks['eyeRightTop']
    eyeRightBottom = faceLandmarks ['eyeRightBottom']
    print ("Eye Left Top:", eyeLeftTop, "Eye Left Bottom:", eyeLeftBottom)
    print ("Eye Right Top:", eyeRightTop, "Eye Right Bottom",eyeRightBottom)

# ;sldjfkl;adjsfl;kadslfjasl;dkjfkl;dsjf

    # face_data = data[0]
    # faceLandmarks = (face_data['faceLandmarks'])
    
    #print (faceLandmarks)
   
    #use classifier (SciKit Learn)
    # eyeLeftTop = faceLandmarks['eyeLeftTop']classifier
    # eyeLeftBottom = faceLandmarks['eyeLeftBottom']
    # eyeRightTop = faceLandmarks['eyeRightTop']
    # eyeRightBottom = faceLandmarks ['eyeRightBottom']
    # occlusion = faceLandmarks ['eyeOccluded']

    # print ("Eye Left Top:", eyeLeftTop, "Eye Left Bottom:", eyeLeftBottom)
    # print ("Eye Right Bottom:", eyeRightTop, "Eye Right Bottom",eyeRightBottom)
    # print (occlusion)
    #can we use occulsion on pupils?

