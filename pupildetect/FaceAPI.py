import requests
import json
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

# images = ['https://cdn.discordapp.com/attachments/413154933278507008/603333810641436682/IMG_20190723_140937.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603333810641436684/IMG_20190723_140941.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603315366583599135/Photo_on_2019-07-23_at_12.59_PM.jpg','https://cdn.discordapp.com/attachments/413154933278507008/603315365212323863/Photo_on_2019-07-23_at_12.59_PM_3.jpg','https://cdn.discordapp.com/attachments/413154933278507008/603326326480568340/IMG_20190723_134117.jpg','https://cdn.discordapp.com/attachments/413154933278507008/603326327277355053/IMG_20190723_134115.jpg']
headers = {'Ocp-Apim-Subscription-Key': subscription_key}


opened = ['https://cdn.discordapp.com/attachments/413154933278507008/603333810641436682/IMG_20190723_140937.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603315366583599135/Photo_on_2019-07-23_at_12.59_PM.jpg' , 'https://cdn.discordapp.com/attachments/413154933278507008/603326327277355053/IMG_20190723_134115.jpg']
closed = ['https://cdn.discordapp.com/attachments/413154933278507008/603333810641436684/IMG_20190723_140941.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603315365212323863/Photo_on_2019-07-23_at_12.59_PM_3.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603326326480568340/IMG_20190723_134117.jpg']
params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}


for image in opened:

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})



    data = response.json()
    face_data = data[0]
    # print (data)
    faceLandmarks = (face_data['faceLandmarks'])


    #print (faceLandmarks)
   
    #use classifier (SciKit Learn)
    # will use right eye once azure is confirmed
    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']
    # eyeRightTop = faceLandmarks['eyeRightTop']
    # eyeRightBottom = faceLandmarks ['eyeRightBottom']
    # print ("Eye Left Top:", eyeLeftTop, "Eye Left Bottom:", eyeLeftBottom)
   

    y1 = (eyeLeftTop['y'])
    y2 = (eyeLeftBottom['y'])

    print ('Open Values:', y2-y1)


print ("\n \n \n " )

for image in closed:

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})



    data = response.json()
    face_data = data[0]
    # print (data)
    faceLandmarks = (face_data['faceLandmarks'])


    #print (faceLandmarks)
   
    #use classifier (SciKit Learn)
    # will use right eye once azure is confirmed
    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']
    # eyeRightTop = faceLandmarks['eyeRightTop']
    # eyeRightBottom = faceLandmarks ['eyeRightBottom']
    # print ("Eye Left Top:", eyeLeftTop, "Eye Left Bottom:", eyeLeftBottom)
   

    y1 = (eyeLeftTop['y'])
    y2 = (eyeLeftBottom['y'])

    print ('Closed Values:', y2-y1)
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

