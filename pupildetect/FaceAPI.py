import requests
import json
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

# images = ['https://cdn.discordapp.com/attachments/413154933278507008/603333810641436682/IMG_20190723_140937.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603333810641436684/IMG_20190723_140941.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603315366583599135/Photo_on_2019-07-23_at_12.59_PM.jpg','https://cdn.discordapp.com/attachments/413154933278507008/603315365212323863/Photo_on_2019-07-23_at_12.59_PM_3.jpg','https://cdn.discordapp.com/attachments/413154933278507008/603326326480568340/IMG_20190723_134117.jpg','https://cdn.discordapp.com/attachments/413154933278507008/603326327277355053/IMG_20190723_134115.jpg']
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

open_list = []
close_list = []

opened = ['https://cdn.discordapp.com/attachments/413154933278507008/603333810641436682/IMG_20190723_140937.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603315366583599135/Photo_on_2019-07-23_at_12.59_PM.jpg' , 'https://cdn.discordapp.com/attachments/413154933278507008/603326327277355053/IMG_20190723_134115.jpg']
closed = ['https://cdn.discordapp.com/attachments/413154933278507008/603333810641436684/IMG_20190723_140941.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603315365212323863/Photo_on_2019-07-23_at_12.59_PM_3.jpg', 'https://cdn.discordapp.com/attachments/413154933278507008/603326326480568340/IMG_20190723_134117.jpg']
params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}

# imgur to azure
# imgurResp = request.post("imgururl", data={"image": file.read(path)})
# request.post("azureurl", data={"url": imgurResp.json()["url"]})

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
    open_values = y2-y1
    open_list.append(open_values)
    


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
    close_values = y2-y1
    close_list.append(close_values)

print("\n \n \n ")

print('Open Values: ', open_list)
print('Close List: ' , close_list)

#number of terms in each list
count_open_list = len(open_list) 
count_close_list = len(close_list)

print("\n \n")
print('There are ', count_open_list, ' terms in the open list.')
print('There are ', count_close_list, ' terms in the close list.')


# while counter < count_open_list:

#     print (position_closed, position_open)
#     if position_closed < position_open:
#         closed_times.append('closed')
#         counter += 1 
#     else:
#         counter += 1
i = 0
counter = 0
for b in range (i, count_open_list):
    # print (counter)
    position_open = (open_list[counter])
    position_closed = (close_list[counter])
    print ([position_closed], [position_open])
    counter += 1



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

