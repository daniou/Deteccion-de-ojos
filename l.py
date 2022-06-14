import cv2
import numpy as np
img = cv2.imread("sample.jpg")
# print(img.shape)
norm = np.zeros((800,800))
norm_image = cv2.normalize(img,img,0,255,cv2.NORM_MINMAX)
cv2.imshow("Low Quality Image",img)
cv2.imshow("Normalized Image",norm_image)
cv2.waitKey(0)