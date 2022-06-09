import numpy as np
import cv2
import pandas as pd


   
img = cv2.imread("sample.jpg")
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
leftEye = img[413:413+32*4, 284:284+4*48]
rightEye = img[413:413+32*4, 550:550+4*48]
leftEye = cv2.resize(leftEye,(48,32))
rightEye = cv2.resize(rightEye,(48,32))
cv2.imwrite('1.jpg', leftEye)
cv2.imwrite('2.jpg', rightEye)