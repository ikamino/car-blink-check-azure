import json
import urllib
import requests

from pprint import pprint
from os.path import expanduser
subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'




assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}


params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}



data = open('C:/Users/Jim Patterson/Desktop/justin.jpg', 'rb')
response = requests.post(face_api_url, data=data, headers=headers)
b = response.json()
face_data = b[0]
print (b)
