import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('me.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

cv2.imshow('image', img) #names our show as 'image' showing our image
cv2.waitKey(0) #waits for any key to be pressedpip
cv2.destroyAllWindows()
