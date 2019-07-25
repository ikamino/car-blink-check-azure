import numpy as np
import cv2
import math
import time

# NOTE: That in order to use this code as is, you require
# a Face and Eye detection Cascade XML files that provide
# openCV the data to do detection

# Set Up/Config

# Fonts
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
fontScale = 1

ERROR_TEXT = 'FACE NOT DETECTED'
ERROR_COLOR = (0,0,255)

# CV Cascades
face_cascade = cv2.CascadeClassifier('faceCascade.xml')
eye_cascade = cv2.CascadeClassifier('eyeCascade.xml')

# Open video stream to main camera device
cap = cv2.VideoCapture(0)

# Time Grabbing Function
currentTimeInMS = lambda: int(round(time.time() * 1000))

startTime = currentTimeInMS()
currentTime = startTime

# Runtime
while(cap.isOpened()):

    # Track delta time
    newTime = currentTimeInMS()
    deltaTime = newTime - currentTime
    currentTime = newTime

    # Capture frame-by-frame
    ret, img = cap.read()

    # Do Face Detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    numFaces = len(faces)
    if (numFaces > 0):
        # Face Found
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            # Do Eye Detection
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    else:
        # Face not detected
        textSize, baseLine = cv2.getTextSize(ERROR_TEXT, font, fontScale, thickness)
        textX = math.floor( (img.shape[1] - textSize[0]) / 2 )
        textY = math.floor(img.shape[0] - (textSize[1] * 2))
        cv2.putText(img, ERROR_TEXT, (textX, textY),font, fontScale, ERROR_COLOR, thickness, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', img)

    # Watch for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()